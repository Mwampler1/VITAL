#
#
# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Kelsey Bare
# kelsey.bare@centauricorp.com
#
# This Python script takes a MUSIC pseudospectrum and plots it using seaborn.heatmap
#
#


# imports
import struct

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors as cols
from PIL import Image


def alpha_cmap(cmap):
    # Create a colormap with alpha components
    my_cmap = cmap(np.arange(cmap.N))
    # Set a square root alpha.
    x = np.linspace(0, 1, cmap.N)
    my_cmap[:, -1] = x ** (2.6)
    my_cmap = cols.ListedColormap(my_cmap)

    return my_cmap


# Open pseudospectrum file from GNURadio-- be sure to change file name
with open("/home/rtp/rtp/GNU-Radio/gr-CARES/apps/IIO_FMCOMMS5/degrees", "rb") as f:
    data1 = struct.unpack('f' * 1024, f.read(4096))

# Convert signal from tuple to array and reshape to plot
new_signal = np.asarray(data1)
new_signal.shape = (1, 1024)

# Plot and save the heatmap
hmap = sns.heatmap(new_signal, cmap=alpha_cmap(plt.cm.get_cmap("jet")), cbar=False)
hmap.tick_params(left=False, labelleft=False, bottom=False)
hmap.set(yticklabels=[], xticklabels=[])
plt.savefig("collectedheatmap.png", transparent=True, bbox_inches="tight")

# Open the background and foreground images--must have same/similar pixel size (this is 515x389)
background = Image.open("new_Room.png")
foreground = Image.open("collectedheatmap.png")

# Overlay the heatmap, show, and save
background.paste(foreground, (0, 0), foreground)
background.show()
background.save("testimage.png")
