import matplotlib as mpl
# Allow matplotlib plots to be rendered without active window manager
mpl.use('agg')

from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
import argparse

from readCPython import load_C_output
from getXi1 import find_root

alpha = 0.00223456 # Solar Radii


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

    args = parser.parse_args()

    R = list()
    m = list()
    for file in args.files:
        state, meta = load_C_output(file)

        xi1, theta_xi1 = find_root(state[0], state[1])

        # convert values to physical units from the dimensionless units
        R.append(alpha*xi1*100)
        m.append(0.09*meta['m'])

    set_style(usetex=args.tex)
    fig, ax = plt.subplots(1, 1, figsize=(10, 7))
    ax.plot(m, R, 'kx')

    ax.set_xlabel(r'Mass [M$_{\odot}$]', fontsize=17)
    ax.set_ylabel(r'R [R$_{\odot}$/100]', fontsize=17)
    plt.savefig(args.output, bbox_inches='tight')

