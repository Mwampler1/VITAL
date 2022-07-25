#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2021 
#
# Authors:
# Kelsey Bare <kelsey.bare@centauricorp.com>
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#


import numpy as np
import seaborn as sns
from gnuradio import gr, qtgui
import sys
from PyQt5 import QtGui
import matplotlib.pyplot as plt




class heatmap_sink_f(gr.sync_block):
    """
    docstring for block heatmap_sink_f
    """

    def __init__(self, vlen=1024, x_start=0, x_stop=180, x_label="X", y_label="Y", title="Direction of Arrival Heatmap",scheme="rocket_r"):
        gr.sync_block.__init__(self,
                               name="heatmap_sink_f",
                               in_sig=[(np.float32, vlen)],
                               out_sig=None)
        self.xstart = x_start
        self.xstop = x_stop
        self.xlabel = x_label
        self.ylabel = y_label
        self.scheme = scheme
        self.title = title



    def work(self, input_items, output_items):
        in0 = input_items[0]
        angles = np.linspace(self.xstart, self.xstop, 29)
        angles = np.around(angles, 0)

        hmap = sns.heatmap(in0, cmap=self.scheme)  # plot the heatmap
        hmap.set_xticklabels(angles)  # set the x-axis to show the angles
        hmap.tick_params(left=False, labelleft=False)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        plt.show()


        return len(input_items[0])
