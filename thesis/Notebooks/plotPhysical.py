import matplotlib as mpl
# Allow matplotlib plots to be rendered without active window manager
mpl.use('Agg')

import numpy as np
import argparse
import matplotlib.pyplot as plt
import pandas as pd

from cycler import cycler




def set_style(usetex=False):
    """ set a proffesional looking matplotlib style

    Keyword Arguments:
        usetex -- use the LaTeX Rendering engine, requires
                  LaTeX to be in the PATH

    """
    default_cycler = (cycler(color=['k', 'b', 'g', 'r']) + cycler(linestyle=['--', ':', '-', '-.']) + cycler(alpha=[0.5, 0.625, 0.75, 0.875]))

    plt.rc('text', usetex=usetex)
    plt.rc('font', family='Serif')
    plt.rc('axes', prop_cycle=default_cycler)


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

if __name__ == "__main__":
    # Argument Parser 
    parser = argparse.ArgumentParser(description='Plot Data')
    parser.add_argument('file', metavar='<path/to/data/files>', type=str, nargs='+', help="Files to plot")
    parser.add_argument('-o', '--output', type=str, default="Figures/ThetaXi.pdf", metavar='<path/to/output/file>', help='output location')
    parser.add_argument('-t', '--tex', action='store_true', help='Use the tex rendering engine when plotting')

    args = parser.parse_args()

    set_style(usetex=args.tex)

    fig, axs = plt.subplots(2, 2, figsize=(20, 20))

    axs[0][0].set_xlabel(r"$\xi$", fontsize=17)
    axs[0][0].set_ylabel(r"$\theta$", fontsize=17)

    axs[1][0].set_xlabel(r"r [cm]", fontsize=17)
    axs[1][0].set_ylabel(r"$\rho$ [g cm$^{-3}$]", fontsize=17)

    axs[0][1].set_xlabel(r"r [cm]", fontsize=17)
    axs[0][1].set_ylabel(r"P [barye]", fontsize=17)

    axs[1][1].set_xlabel(r"r [cm]", fontsize=17)
    axs[1][1].set_ylabel(r"T [K]", fontsize=17)

    # plot each file as a differnt curve
    for file in args.file:
        data = np.load(file)
        label=file.split('/')[-1].split('.')[0]

        axs[0][0].plot(data[0], data[1], label=label)
        axs[1][0].plot(data[3], data[4], label=label)
        axs[0][1].plot(data[3], data[5], label=label)
        axs[1][1].plot(data[3], data[6], label=label)

    axs[0][0].legend()
    axs[0][1].legend()
    axs[1][0].legend()
    axs[1][1].legend()

    plt.savefig(args.output, bbox_inches='tight')
