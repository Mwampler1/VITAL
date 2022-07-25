#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: MUSIC Simulation Test
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import CARES
import aoa
import numpy
from gnuradio import qtgui

class MUSIC_test(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "MUSIC Simulation Test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("MUSIC Simulation Test")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "MUSIC_test")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.theta0_deg = theta0_deg = 40
        self.NumArrayElements = NumArrayElements = 4
        self.NormSpacing = NormSpacing = 0.5
        self.theta0 = theta0 = numpy.pi*theta0_deg/180
        self.ant_locs = ant_locs = numpy.dot(NormSpacing, numpy.arange(NumArrayElements/2, -NumArrayElements/2, -1) if (NumArrayElements%2==1) else numpy.arange(NumArrayElements/2-0.5, -NumArrayElements/2-0.5, -1))
        self.amv0 = amv0 = numpy.exp(-1j*ant_locs*2*numpy.pi*numpy.cos(theta0))
        self.sample_rate = sample_rate = 1e6
        self.array_manifold_matrix = array_manifold_matrix = numpy.array([amv0, amv0]).transpose()
        self.NumTargets = NumTargets = 2

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_vector_sink_f_0_0_0_0 = qtgui.vector_sink_f(
            1024,
            0,
            180/1024,
            "AC",
            "y-Axis",
            "",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0_0_0_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0_0_0_0.set_y_axis(-140, 10)
        self.qtgui_vector_sink_f_0_0_0_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0_0_0_0.enable_grid(False)
        self.qtgui_vector_sink_f_0_0_0_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0_0_0_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0_0_0_0.set_ref_level(0)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_0_0_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_vector_sink_f_0_0_0_0_win)
        self.qtgui_vector_sink_f_0_0_0 = qtgui.vector_sink_f(
            1024,
            0,
            180/1024,
            "BD",
            "y-Axis",
            "",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0_0_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0_0_0.set_y_axis(-140, 10)
        self.qtgui_vector_sink_f_0_0_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0_0_0.enable_grid(False)
        self.qtgui_vector_sink_f_0_0_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0_0_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0_0_0.set_ref_level(0)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0_0_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0_0_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0_0_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_0_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_vector_sink_f_0_0_0_win)
        self.qtgui_vector_sink_f_0_0 = qtgui.vector_sink_f(
            1024,
            0,
            180/1024,
            "CD",
            "y-Axis",
            "",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0_0.set_y_axis(-140, 10)
        self.qtgui_vector_sink_f_0_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0_0.enable_grid(False)
        self.qtgui_vector_sink_f_0_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0_0.set_ref_level(0)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_vector_sink_f_0_0_win)
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            1024,
            0,
            180/1024,
            "AB",
            "y-Axis",
            "",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis(-140, 10)
        self.qtgui_vector_sink_f_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0.enable_grid(False)
        self.qtgui_vector_sink_f_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0.set_ref_level(0)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_vector_sink_f_0_win)
        self.qtgui_number_sink_0_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0_0_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0_0_0.set_title("")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0_0_0_0.set_min(i, -1)
            self.qtgui_number_sink_0_0_0_0.set_max(i, 1)
            self.qtgui_number_sink_0_0_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_0_0_0_win)
        self.qtgui_number_sink_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0_0.set_title("")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0_0_0.set_min(i, -1)
            self.qtgui_number_sink_0_0_0.set_max(i, 1)
            self.qtgui_number_sink_0_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_0_0_win)
        self.qtgui_number_sink_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0.set_title("")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0_0.set_min(i, -1)
            self.qtgui_number_sink_0_0.set_max(i, 1)
            self.qtgui_number_sink_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_0_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0.set_min(i, -1)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_win)
        self.blocks_throttle_0_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, sample_rate,True)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, sample_rate,True)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_multiply_matrix_xx_0 = blocks.multiply_matrix_cc(array_manifold_matrix, gr.TPP_ALL_TO_ALL)
        self.blocks_file_sink_0_0_0_0_1_0_0_0 = blocks.file_sink(gr.sizeof_float*1, '/home/megan/CARES/CD_angle', False)
        self.blocks_file_sink_0_0_0_0_1_0_0_0.set_unbuffered(False)
        self.blocks_file_sink_0_0_0_0_1_0_0 = blocks.file_sink(gr.sizeof_float*1, '/home/megan/CARES/BD_angle', False)
        self.blocks_file_sink_0_0_0_0_1_0_0.set_unbuffered(False)
        self.blocks_file_sink_0_0_0_0_1_0 = blocks.file_sink(gr.sizeof_float*1, '/home/megan/CARES/AC_angle', False)
        self.blocks_file_sink_0_0_0_0_1_0.set_unbuffered(False)
        self.blocks_file_sink_0_0_0_0_1 = blocks.file_sink(gr.sizeof_float*1, '/home/megan/CARES/AB_angle', False)
        self.blocks_file_sink_0_0_0_0_1.set_unbuffered(False)
        self.blocks_file_sink_0_0_0_0_0_0_0 = blocks.file_sink(gr.sizeof_float*1024, '/home/megan/CARES/AC_data', False)
        self.blocks_file_sink_0_0_0_0_0_0_0.set_unbuffered(False)
        self.blocks_file_sink_0_0_0_0_0_0 = blocks.file_sink(gr.sizeof_float*1024, '/home/megan/CARES/BD_data', False)
        self.blocks_file_sink_0_0_0_0_0_0.set_unbuffered(False)
        self.blocks_file_sink_0_0_0_0_0 = blocks.file_sink(gr.sizeof_float*1024, '/home/megan/CARES/CD_data', False)
        self.blocks_file_sink_0_0_0_0_0.set_unbuffered(False)
        self.blocks_file_sink_0_0_0_0 = blocks.file_sink(gr.sizeof_float*1024, '/home/megan/CARES/AB_data', False)
        self.blocks_file_sink_0_0_0_0.set_unbuffered(False)
        self.blocks_add_xx_0_0 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.aoa_autocorrelate_0_0_0_0 = aoa.correlate(2, 1024, 512, 0)
        self.aoa_autocorrelate_0_0_0 = aoa.correlate(2, 1024, 512, 0)
        self.aoa_autocorrelate_0_0 = aoa.correlate(2, 1024, 512, 0)
        self.aoa_autocorrelate_0 = aoa.correlate(2, 1024, 512, 0)
        self.aoa_MUSIC_lin_array_0_0_0_0 = aoa.MUSIC_lin_array(NormSpacing, 1, 2, 1024)
        self.aoa_MUSIC_lin_array_0_0_0 = aoa.MUSIC_lin_array(NormSpacing, 1, 2, 1024)
        self.aoa_MUSIC_lin_array_0_0 = aoa.MUSIC_lin_array(NormSpacing, 1, 2, 1024)
        self.aoa_MUSIC_lin_array_0 = aoa.MUSIC_lin_array(NormSpacing, 1, 2, 1024)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(sample_rate, analog.GR_COS_WAVE, 30E+3, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(sample_rate, analog.GR_COS_WAVE, 10E+3, 1, 0, 0)
        self.analog_noise_source_x_1 = analog.noise_source_c(analog.GR_GAUSSIAN, .100, 3135154)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, .100, 972353)
        self.CARES_find_local_max_0_0_0_0 = CARES.find_local_max(1, 1024, 0.0, 180.0)
        self.CARES_find_local_max_0_0_0 = CARES.find_local_max(1, 1024, 0.0, 180.0)
        self.CARES_find_local_max_0_0 = CARES.find_local_max(1, 1024, 0.0, 180.0)
        self.CARES_find_local_max_0 = CARES.find_local_max(1, 1024, 0.0, 180.0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.CARES_find_local_max_0, 1), (self.blocks_file_sink_0_0_0_0_1, 0))
        self.connect((self.CARES_find_local_max_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.CARES_find_local_max_0, 1), (self.qtgui_number_sink_0, 0))
        self.connect((self.CARES_find_local_max_0_0, 1), (self.blocks_file_sink_0_0_0_0_1_0_0_0, 0))
        self.connect((self.CARES_find_local_max_0_0, 0), (self.blocks_null_sink_0, 3))
        self.connect((self.CARES_find_local_max_0_0, 1), (self.qtgui_number_sink_0_0, 0))
        self.connect((self.CARES_find_local_max_0_0_0, 1), (self.blocks_file_sink_0_0_0_0_1_0_0, 0))
        self.connect((self.CARES_find_local_max_0_0_0, 0), (self.blocks_null_sink_0, 2))
        self.connect((self.CARES_find_local_max_0_0_0, 1), (self.qtgui_number_sink_0_0_0, 0))
        self.connect((self.CARES_find_local_max_0_0_0_0, 1), (self.blocks_file_sink_0_0_0_0_1_0, 0))
        self.connect((self.CARES_find_local_max_0_0_0_0, 0), (self.blocks_null_sink_0, 1))
        self.connect((self.CARES_find_local_max_0_0_0_0, 1), (self.qtgui_number_sink_0_0_0_0, 0))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.analog_noise_source_x_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.aoa_MUSIC_lin_array_0, 0), (self.CARES_find_local_max_0, 0))
        self.connect((self.aoa_MUSIC_lin_array_0, 0), (self.blocks_file_sink_0_0_0_0, 0))
        self.connect((self.aoa_MUSIC_lin_array_0, 0), (self.qtgui_vector_sink_f_0, 0))
        self.connect((self.aoa_MUSIC_lin_array_0_0, 0), (self.CARES_find_local_max_0_0, 0))
        self.connect((self.aoa_MUSIC_lin_array_0_0, 0), (self.blocks_file_sink_0_0_0_0_0, 0))
        self.connect((self.aoa_MUSIC_lin_array_0_0, 0), (self.qtgui_vector_sink_f_0_0, 0))
        self.connect((self.aoa_MUSIC_lin_array_0_0_0, 0), (self.CARES_find_local_max_0_0_0, 0))
        self.connect((self.aoa_MUSIC_lin_array_0_0_0, 0), (self.blocks_file_sink_0_0_0_0_0_0, 0))
        self.connect((self.aoa_MUSIC_lin_array_0_0_0, 0), (self.qtgui_vector_sink_f_0_0_0, 0))
        self.connect((self.aoa_MUSIC_lin_array_0_0_0_0, 0), (self.CARES_find_local_max_0_0_0_0, 0))
        self.connect((self.aoa_MUSIC_lin_array_0_0_0_0, 0), (self.blocks_file_sink_0_0_0_0_0_0_0, 0))
        self.connect((self.aoa_MUSIC_lin_array_0_0_0_0, 0), (self.qtgui_vector_sink_f_0_0_0_0, 0))
        self.connect((self.aoa_autocorrelate_0, 0), (self.aoa_MUSIC_lin_array_0, 0))
        self.connect((self.aoa_autocorrelate_0_0, 0), (self.aoa_MUSIC_lin_array_0_0, 0))
        self.connect((self.aoa_autocorrelate_0_0_0, 0), (self.aoa_MUSIC_lin_array_0_0_0, 0))
        self.connect((self.aoa_autocorrelate_0_0_0_0, 0), (self.aoa_MUSIC_lin_array_0_0_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0_0_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.blocks_multiply_matrix_xx_0, 0), (self.aoa_autocorrelate_0, 0))
        self.connect((self.blocks_multiply_matrix_xx_0, 1), (self.aoa_autocorrelate_0, 1))
        self.connect((self.blocks_multiply_matrix_xx_0, 2), (self.aoa_autocorrelate_0_0, 0))
        self.connect((self.blocks_multiply_matrix_xx_0, 3), (self.aoa_autocorrelate_0_0, 1))
        self.connect((self.blocks_multiply_matrix_xx_0, 3), (self.aoa_autocorrelate_0_0_0, 1))
        self.connect((self.blocks_multiply_matrix_xx_0, 1), (self.aoa_autocorrelate_0_0_0, 0))
        self.connect((self.blocks_multiply_matrix_xx_0, 2), (self.aoa_autocorrelate_0_0_0_0, 1))
        self.connect((self.blocks_multiply_matrix_xx_0, 0), (self.aoa_autocorrelate_0_0_0_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_multiply_matrix_xx_0, 0))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.blocks_multiply_matrix_xx_0, 1))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "MUSIC_test")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_theta0_deg(self):
        return self.theta0_deg

    def set_theta0_deg(self, theta0_deg):
        self.theta0_deg = theta0_deg
        self.set_theta0(numpy.pi*self.theta0_deg/180)

    def get_NumArrayElements(self):
        return self.NumArrayElements

    def set_NumArrayElements(self, NumArrayElements):
        self.NumArrayElements = NumArrayElements
        self.set_ant_locs(numpy.dot(self.NormSpacing, numpy.arange(self.NumArrayElements/2, -self.NumArrayElements/2, -1) if (self.NumArrayElements%2==1) else numpy.arange(self.NumArrayElements/2-0.5, -self.NumArrayElements/2-0.5, -1)))

    def get_NormSpacing(self):
        return self.NormSpacing

    def set_NormSpacing(self, NormSpacing):
        self.NormSpacing = NormSpacing
        self.set_ant_locs(numpy.dot(self.NormSpacing, numpy.arange(self.NumArrayElements/2, -self.NumArrayElements/2, -1) if (self.NumArrayElements%2==1) else numpy.arange(self.NumArrayElements/2-0.5, -self.NumArrayElements/2-0.5, -1)))

    def get_theta0(self):
        return self.theta0

    def set_theta0(self, theta0):
        self.theta0 = theta0
        self.set_amv0(numpy.exp(-1j*self.ant_locs*2*numpy.pi*numpy.cos(self.theta0)))

    def get_ant_locs(self):
        return self.ant_locs

    def set_ant_locs(self, ant_locs):
        self.ant_locs = ant_locs
        self.set_amv0(numpy.exp(-1j*self.ant_locs*2*numpy.pi*numpy.cos(self.theta0)))

    def get_amv0(self):
        return self.amv0

    def set_amv0(self, amv0):
        self.amv0 = amv0
        self.set_array_manifold_matrix(numpy.array([self.amv0, self.amv0]).transpose())

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.sample_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.sample_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.sample_rate)
        self.blocks_throttle_0_0_0.set_sample_rate(self.sample_rate)

    def get_array_manifold_matrix(self):
        return self.array_manifold_matrix

    def set_array_manifold_matrix(self, array_manifold_matrix):
        self.array_manifold_matrix = array_manifold_matrix
        self.blocks_multiply_matrix_xx_0.set_A(self.array_manifold_matrix)

    def get_NumTargets(self):
        return self.NumTargets

    def set_NumTargets(self, NumTargets):
        self.NumTargets = NumTargets



def main(top_block_cls=MUSIC_test, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
