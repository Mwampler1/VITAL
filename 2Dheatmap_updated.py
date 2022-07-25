#
#
# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Michael Wampler
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



# Open the background and foreground images--must have same/similar pixel size (this is 515x389)
background = Image.open("testimage.png")
#image = Image.open("transparent_rotated_image.png", transparent=True)

foreground = Image.open("rotated_image_final.png")

#make image transparent (PIL import uses putalpha)
foreground.putalpha(50)

#foreground = foreground1.rotate(90)
#foreground = plt.savefig(foreground3, transparent=True, bbox_inches="tight")

# Overlay the heatmap, show, and save
background.paste(foreground, (0, 0), foreground)
background.show()
background.save("testimage_horiz_and_vert.png")
