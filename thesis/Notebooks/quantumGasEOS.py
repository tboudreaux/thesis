import matplotlib as mpl
# Allow matplotlib plots to be rendered without active window manager
mpl.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
import argparse

Kn = 3.166e12 # g^(-2/3) cm^6 s^-2
Kr = 4.936e14 # g^(-2/3) cm^6 s^-2
rho_0 = (Kr/Kn)**3


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

def P_N(rho):
    """Equation of state for a degenerate fermi-gas in the non relativistic case

    Positional Arguments:
        rho -> density in cgs units
    Returns:
        P -> Pressure in cgs units
    """

    return Kn*rho**(5/3)


def P_R(rho):
    """Equation of state for a degenerate fermi-gas in the relativistic case

    Positional Arguments:
        rho -> density in cgs units
    Returns:
        P -> Pressure in cgs units
    """

    return Kr*rho**(4/3)

def P(rho):
    """Approximate equation of state of a degenerate fermi-gas for both the
       relativistic and non relativistic case

    Positional Arguments:
        rho -> density in cgs units
    Returns:
        Pressure -> Pressure in cgs units
    """

    return P_N(rho)/np.sqrt(1+(rho/rho_0)**(2/3))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot the Equations of state for the three cases of a degenerate fermi-gas")
    parser.add_argument('--ri', type=float, help='initial rho in cgs')
    parser.add_argument('--rf', type=float, help='final rho in cgs')
    parser.add_argument('-n', '--num', type=int, help='size of the rho array in cgs')
    parser.add_argument('-o', '--output', type=str, help='path to save figure to, if not provided will write data to standard output', default='NULL')
    parser.add_argument('-t', '--tex', action='store_true', help='Use the tex rendering engine when plotting')

    args = parser.parse_args()

    rho = np.linspace(args.ri, args.rf, args.num)
    pn = P_N(rho)
    pr = P_R(rho)
    p = P(rho)

    # Write to standard output if figure output is not provided
    if args.output == 'NULL':
        print('rho,PN,PR,P')
        for r, p_n, p_r, p_p in zip(rho, pn, pr, p):
            print("{},{},{},{}".format(r, p_n, p_r, p_p))
    else:
        set_style(usetex=args.tex)

        fig, ax = plt.subplots(1, 1, figsize=(10, 7))
        ax.loglog(rho, pn, label=r'$P_{N}$', linestyle='-', color='black')
        ax.loglog(rho, pr, label=r'$P_{R}$', linestyle='--', color='black')
        ax.loglog(rho, p, label=r'$P$', linestyle='-.', color='black')

        ax.set_xlabel(r'$\rho$ [g cm$^{-3}$]', fontsize=17)
        ax.set_ylabel(r'$P$ [barye]', fontsize=17)
        ax.legend(loc='best')

        plt.savefig(args.output, bbox_inches='tight')
