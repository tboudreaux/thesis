import matplotlib as mpl
# Allow matplotlib plots to be rendered without active window manager
mpl.use('agg')

from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

from readCPython import load_C_output
import argparse


def set_style(usetex=False):
    """ set a proffesional looking matplotlib style

    Keyword Arguments:
        usetex -- use the LaTeX Rendering engine, requires
                  LaTeX to be in the PATH

    """
    plt.rc('text', usetex=usetex)
    plt.rc('font', family='Serif')


    mpl.rcParams['figure.figsize'] = [10, 7]
    mpl.rcParams['font.size'] = 17

    mpl.rcParams['savefig.dpi'] = 150
    mpl.rcParams['xtick.minor.visible'] = True
    mpl.rcParams['ytick.minor.visible'] = True
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'

    mpl.rcParams['xtick.top'] = True
    mpl.rcParams['ytick.right'] = True

    mpl.rcParams['xtick.major.size'] = 6
    mpl.rcParams['xtick.minor.size'] = 3

    mpl.rcParams['ytick.major.size'] = 6
    mpl.rcParams['ytick.minor.size'] = 3

    mpl.rcParams['xtick.labelsize'] = 13
    mpl.rcParams['ytick.labelsize'] = 13

logistic = lambda x, a, b, c: a/(1+np.exp(-(c*x-b)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot WD Mass vs Central Density")
    parser.add_argument("files", nargs="+", type=str, help="Path to file")
    parser.add_argument("-o", "--output", type=str, help="save path")
    parser.add_argument('-t', '--tex', action='store_true', help='Use the tex rendering engine when plotting')
    parser.add_argument('-f', '--fit', action='store_true', help='Fit a Logistic Function to get a value for the asymptote')

    args = parser.parse_args()

    rho_c = list()
    m = list()
    for file in args.files:
        state, meta = load_C_output(file, oh=True)

        # convert value to physical units from the dimensionless values
        rho_c.append(3.789e6*meta['theta_c'])
        m.append(0.09*meta['m'])

    set_style(usetex=args.tex)
    fig, ax = plt.subplots(1, 1, figsize=(10, 7))
    ax.semilogx(rho_c, m, 'kx')

    # fit a logistic function to extract verticle asymptote
    if args.fit:
        fit, covar = curve_fit(logistic, np.log10(rho_c), m)
        err = np.sqrt(np.diag(covar))
        RHO_C = np.logspace(np.log10(min(rho_c)), np.log10(max(rho_c)), 100)
        ax.semilogx(RHO_C, logistic(np.log10(RHO_C), *fit), alpha=0.5, color='black')
        print("Max Stable Mass: {:0.2f}pm{:0.3f} M_solar".format(fit[0], err[0]))

    ax.set_ylabel(r'Mass [M$_{\odot}$]', fontsize=17)
    ax.set_xlabel(r'Central Density [g cm$^{-3}$]', fontsize=17)
    plt.savefig(args.output, bbox_inches='tight')

