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

# Open pseudospectrum file from GNURadio-- be sure to change the file name/path
with open("/home/rtp/rtp/GNU-Radio/gr-CARES/apps/IIO_FMCOMMS5/degreeshoriz", "rb") as f:
    data1 = struct.unpack('f' * 1024, f.read(4096))

# Convert signal from tuple to array and reshape the data
new_signal = np.asarray(data1)
new_signal.shape = (1, 1024)

# Generate angle values for the x-axis
angles = np.linspace(0, 180, 29)
angles = np.around(angles, 0)

# Plot the heatmap
hmap = sns.heatmap(new_signal, cmap="jet")
hmap.set(xticklabels=angles, yticklabels=[])
hmap.tick_params(left=False, labelleft=False)
plt.xlabel("Angle (Degrees)")
plt.title("Angle of Arrival: Degrees")
plt.show()
#plt.imsave("1D_heatmap_image")
