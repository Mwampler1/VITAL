#
#
# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Authors: Kelsey Bare and Megan Riley
# kelsey.bare@centauricorp.com
# megan.riley@centauricorp.com
#
# This Python script simulates a 2D AoA and overlays it on a ruined house using doatools.py
#
# REQUIRED: doatools.py https://github.com/morriswmz/doatools.py
#
#


import doatools.estimation as estimation
import doatools.model as model
import doatools.plotting as doaplot

import matplotlib.colors as cols
import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const
from PIL import Image


def alpha_cmap(cmap):
    # Create a colormap with alpha components
    my_cmap = cmap(np.arange(cmap.N))
    # Set a square root alpha.
    x = np.linspace(0, 1, cmap.N)
    my_cmap[:, -1] = x ** 2.6
    my_cmap = cols.ListedColormap(my_cmap)

    return my_cmap


# constants
fc = 2400  # frequency of signal
c = const.speed_of_light
lam = c / fc
fs = 8000
wavelength = lam  # Normalized wavelength
d0 = wavelength / 2
power_source = 1.0
power_noise = 1.0  # SNR = 0 dB
n_snapshots = 512

# Create a 16-element URA
ura = model.UniformRectangularArray(4, 4, d0)

# Place a far-field source at (50, 40)
sources = model.FarField2DSourcePlacement(locations=[(50, 40)], unit='deg')

# Use the stochastic signal model.
source_signal = model.ComplexStochasticSignal(sources.size, power_source)
noise_signal = model.ComplexStochasticSignal(ura.size, power_noise)

# Get the estimated covariance matrix.
_, R = model.get_narrowband_snapshots(ura, sources, wavelength, source_signal, noise_signal,
                                      n_snapshots, return_covariance=True)

# Create a MUSIC-based estimator.
grid = estimation.FarField2DSearchGrid(unit='deg', start=(0, 0), stop=(90, 90))
estimator = estimation.MUSIC(ura, wavelength, grid)

# Get the estimates.
resolved, estimates, sp = estimator.estimate(R, sources.size, return_spectrum=True, refine_estimates=True,
                                             refinement_density=10, refinement_iters=3)

# Plot the MUSIC-spectrum. Comment out line 183 from plot_spectrum.py from doatools.py to remove the color bar
ax = plt.subplot(1, 1, 1)
doaplot.plot_spectrum(sp, grid, ax=ax, use_log_scale=True, color_map=alpha_cmap(plt.cm.get_cmap("jet")), )
plt.axis('off')
plt.savefig('testimage.png', bbox_inches='tight', transparent=True)

# Open the two images, overlay the two, and save
background = Image.open("new_Room.png")
background = Image.open("testimage.png")
foreground = Image.open("testimage.png")
background.paste(foreground, (0, 0), foreground)
background.show()
background.save("housesimulation.png")
