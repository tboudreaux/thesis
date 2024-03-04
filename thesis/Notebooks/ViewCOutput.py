import matplotlib as mpl
# Allow matplotlib plots to be rendered without active window manager
mpl.use('agg')

from readCPython import load_C_output
from getXi1 import find_root


import matplotlib.pyplot as plt
import numpy as np
import os
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


def extract_theta_dot_xi(dataFiles):
    """ return the polytroic index assosiated solution for every given binary file path

    Positional Arguments:
        dataFiles -- iterator of path to binary data files produced from c executable itegrate

    Returns -> (N, STATE):
        STATE -- List of data from binary file paths (parallel to N)
        META -- Metadata extracted from header of dump files
    """
    STATE = list()
    META = list()
    for dataFile in dataFiles:
        state, metadata = load_C_output(dataFile)
        META.append(metadata)
        STATE.append(state)
    return STATE, META


if __name__ == '__main__':
    # Argument Parser 
    parser = argparse.ArgumentParser(description='Plot Data')
    parser.add_argument('files', metavar='<path/to/data/files>', type=str, nargs='+', help="Files to plot")
    parser.add_argument('-o', '--output', type=str, default="Figures/ThetaXi.pdf", metavar='<path/to/output/file>', help='output location')
    parser.add_argument('-r', '--root',  action='store_true', help='Also plot the crosshairs showing xi1')
    parser.add_argument('-t', '--tex', action='store_true', help='Use the tex rendering engine when plotting')
    parser.add_argument('-d', '--derivitive', action='store_true', help='Plot dtheta/dxi along with theta')
    parser.add_argument('-k', '--key', action='store_true', help='Include a key/legend in the output graph')
    parser.add_argument('-l', '--log', action='store_true', help='plot on a semilogy scale')

    args = parser.parse_args()

    # Filter Given paths to only select .binary files
    dataFiles = filter(lambda x: '.dat' in x, args.files)

    # Set the style to include minor ticks, larger labels, and ticks on all sides
    set_style(usetex=args.tex)


    # Plot all Given Solutions
    fig, ax = plt.subplots(1, 1, figsize=(10, 7))
    for file in dataFiles:
        state, meta = load_C_output(file)
        # deal with either degenerate or non degenerate identifier
        if 'n' in meta:
            identifier = meta['n']
        else:
            identifier = meta['theta_c']
        # deal with either log or non log plotting
        if args.log:
            ax.semilogy(state[0], state[1], label=r"$\theta_{{{}}}$".format(identifier), color='black')
        else:
            ax.plot(state[0], state[1], label=r"$\theta_{{{}}}$".format(identifier), color='black')
        if args.derivitive:
            if args.log:
                ax.semilogy(state[0], state[2], linestyle='--', label=r"$\left(\frac{{d\theta}}{{d\xi}}\right)_{{{}}}$".format(identifier), color='black')
            else:
                ax.plot(state[0], state[2], linestyle='--', label=r"$\left(\frac{{d\theta}}{{d\xi}}\right)_{{{}}}$".format(identifier), color='black')
        # If requested show where each solution has its root
        if args.root:
            xi1Approx, theta1Approx = find_root(state[0], state[1])
            ax.axvline(x=xi1Approx, linestyle=':', color='black', alpha=0.5)
            ax.axhline(y=0, linestyle=':', color='black', alpha=0.5)
        # explicitly clear data when plotting multiple solutions in an attempt to keep the memory manager happy
        # does not help in most cases because the python GC is pretty okay but no harm in being explicit here
        del state
        del meta
    ax.set_xlabel(r'$\xi$', fontsize=17)
    ax.set_ylabel(r'$\theta$, $\frac{d\theta}{d\xi}$', fontsize=17)
    if args.key:
        plt.legend()

    # Save File to requested Location
    plt.savefig(args.output, bbox_inches='tight')
