from pysep.io.trk.read import read_trk
from pysep.io.mod.read import read_bin_mod

import argparse

import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np
import os

def setup_fancy_plot():
	plt.rc('text', usetex=True)
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


def Kippenhan_Iben(age, radius, convectiveMask, ageTrk, Teff, L, R, He3):
    fig, ax = plt.subplots(1, 1, figsize=(10, 7))

    axes = [ax, ax.twinx(), ax.twinx(), ax.twinx(), ax.twinx()]
    # fig.subplots_adjust(right=0.75)

    axes[2].spines['right'].set_position(('axes', 1.6))
    axes[3].spines['right'].set_position(('axes', 1.4))
    axes[4].spines['right'].set_position(('axes', 1.2))

    axes[2].set_frame_on(True)
    axes[2].patch.set_visible(False)
    axes[3].set_frame_on(True)
    axes[3].patch.set_visible(False)
    axes[4].set_frame_on(True)
    axes[4].patch.set_visible(False)

    colors = ('C0', 'C1', 'C2', 'C3')
    axes[0].pcolormesh(age, radius, convectiveMask.T, hatch='/', cmap=mpl.cm.get_cmap('binary_r'))
    axes[0].set_xlabel('Age [Gyr]', fontsize=27)
    axes[0].set_ylabel('Radius Fraction', fontsize=27)

    axes[1].plot(ageTrk, Teff, color=colors[0])
    axes[1].set_ylabel(r'Log[$T_{core}$]', fontsize=27, color=colors[0])
    axes[1].tick_params(axis='y', colors=colors[0])

    axes[2].plot(ageTrk, L, color=colors[1])
    axes[2].set_ylabel(r'L/L$_{ZAMS}$', fontsize=27, color=colors[1])
    axes[2].tick_params(axis='y', colors=colors[1])

    axes[3].plot(ageTrk, R, color=colors[2])
    axes[3].set_ylabel(r'R/R$_{ZAMS}$', fontsize=27, color=colors[2])
    axes[3].tick_params(axis='y', colors=colors[2])

    axes[4].plot(ageTrk, He3, color=colors[3])
    axes[4].set_ylabel(r'X($^{3}$He)$_{core}$', fontsize=27, color=colors[3])
    axes[4].tick_params(axis='y', colors=colors[3])

    return fig, axes


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="generate kippenhan-Iben diagram for a model")
    parser.add_argument("path", help="path to model directory", type=str)
    parser.add_argument("-o", "--output", help="path to save diagram too", default="Kippenhan_Iben.pdf", type=str)

    args = parser.parse_args()

    setup_fancy_plot()

    files = os.listdir(args.path)
    binMods = filter(lambda x: x.endswith('.binmod'), files)
    trks = filter(lambda x: x.endswith('.track'), files)

    binModFile = next(binMods)
    trkFile = next(trks)

    binModPath = os.path.join(args.path, binModFile)
    trkPath = os.path.join(args.path, trkFile)

    headers, cards = read_bin_mod(binModPath)
    trks, metas = read_trk(trkPath)
    trk = trks[0]

    minAge = 0.1
    maxAge = 12

    age = headers[:, 1]
    ageMask = age[(age <= maxAge) & (age >= minAge)]

    trkAgeCond = (trk['AGE'] <= maxAge) & (trk['AGE'] >= minAge)
    trkAge = trk['AGE'][trkAgeCond]

    ClogT = trk['C_log_T']
    Teff = ClogT[trkAgeCond]

    LLZAMS = ((10**trk['log_L'])/(10**trk.iloc[0]['log_L']))[trkAgeCond]

    RRZAMS = ((10**trk['log_R'])/(10**trk.iloc[0]['log_R']))[trkAgeCond]

    He3 = trk['CA_He3'][trkAgeCond]


    convectiveMask = cards[:, 5, :]
    radius = np.linspace(0, 1, convectiveMask.T.shape[0])

    radiusCut = 0.05

    convectiveMaskF = convectiveMask[(age <= maxAge) & (age >= minAge)]
    convectiveMaskF = convectiveMaskF[:,radius < radiusCut]

    fig, axes = Kippenhan_Iben(ageMask, radius[radius < radiusCut], convectiveMaskF, trkAge, Teff, LLZAMS, RRZAMS, He3)

    fig.savefig(args.output, bbox_inches="tight")

