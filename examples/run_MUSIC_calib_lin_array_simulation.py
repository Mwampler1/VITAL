#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Run Music Calib Lin Array Simulation
# GNU Radio version: 3.8.2.0

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

def struct(data): return type('Struct', (object,), data)()
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
from gnuradio.qtgui import Range, RangeWidget
import CARES
import aoa
import numpy
import os

from gnuradio import qtgui

class run_MUSIC_calib_lin_array_simulation(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Run Music Calib Lin Array Simulation")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Run Music Calib Lin Array Simulation")
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

        self.settings = Qt.QSettings("GNU Radio", "run_MUSIC_calib_lin_array_simulation")

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
        self.theta1_deg = theta1_deg = 123
        self.theta0_deg = theta0_deg = 30
        self.num_array_elements = num_array_elements = 4
        self.theta1 = theta1 = numpy.pi*theta1_deg/180
        self.theta0 = theta0 = numpy.pi*theta0_deg/180
        self.ant_phases = ant_phases = numpy.array([ 0.28647672,  5.27248071,  2.71271102,  1.36970886])
        self.ant_locs = ant_locs = numpy.dot(0.5, numpy.arange(num_array_elements/2, -num_array_elements/2, -1) if (num_array_elements%2==1) else numpy.arange(num_array_elements/2-0.5, -num_array_elements/2-0.5, -1))
        self.ant_gains = ant_gains = numpy.array([ 0.94984789,  0.4544107 ,  0.34649469,  0.25083929])
        self.ant_coeffs = ant_coeffs = ant_gains*numpy.exp(1j*ant_phases)
        self.amv1_true = amv1_true = numpy.exp(-1j*ant_locs*2*numpy.pi*numpy.cos(theta1))
        self.amv0_true = amv0_true = numpy.exp(-1j*ant_locs*2*numpy.pi*numpy.cos(theta0))
        self.directory_config_files = directory_config_files = "/home/rtp/rtp/GNU-Radio/gr-CARES/examples"
        self.antenna_calibration = antenna_calibration = "calibration_lin_array_simulated.cfg"
        self.amv1 = amv1 = numpy.multiply(ant_coeffs, amv1_true)
        self.amv0 = amv0 = numpy.multiply(ant_coeffs, amv0_true)
        self.tone_freq_2 = tone_freq_2 = 20000
        self.tone_freq_1 = tone_freq_1 = 10000
        self.snapshot_size = snapshot_size = 2048
        self.sample_rate = sample_rate = 320000
        self.pspectrum_length = pspectrum_length = 1024
        self.overlap_size = overlap_size = 512
        self.num_targets = num_targets = 2
        self.norm_spacing = norm_spacing = 0.500
        self.input_variables = input_variables = struct({

            'SampleRate': 320000,

            'ToneFreq1': 10000,

            'ToneFreq2': 20000,

            'NormSpacing': 0.5,

            'NumTargets': 2,

            'NumArrayElements': 4,

            'PSpectrumLength': 2**10,

            'SnapshotSize': 2**11,

            'OverlapSize': 2**9,

            'AntGains': numpy.array([ 0.94984789,  0.4544107 ,  0.34649469,  0.25083929]),

            'AntPhases': numpy.array([ 0.28647672,  5.27248071,  2.71271102,  1.36970886]),

            'DirectoryConfigFiles': "/tmp",

            'AntennaCalibration': "calibration_lin_array_simulated.cfg",







        })
        self.array_manifold_matrix = array_manifold_matrix = numpy.array([amv0, amv1]).transpose()
        self.antenna_calibration_file_name = antenna_calibration_file_name = os.path.join(directory_config_files, antenna_calibration)

        ##################################################
        # Blocks
        ##################################################
        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, 'Pseudo-Spectrum')
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, 'Direction of Arrival')
        self.tab_widget_2 = Qt.QWidget()
        self.tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_2)
        self.tab_grid_layout_2 = Qt.QGridLayout()
        self.tab_layout_2.addLayout(self.tab_grid_layout_2)
        self.tab.addTab(self.tab_widget_2, 'Direction of Arrival')
        self.top_grid_layout.addWidget(self.tab)
        self._theta1_deg_range = Range(0, 180, 1, 123, 200)
        self._theta1_deg_win = RangeWidget(self._theta1_deg_range, self.set_theta1_deg, 'AoA', "counter_slider", float)
        self.top_grid_layout.addWidget(self._theta1_deg_win)
        self._theta0_deg_range = Range(0, 180, 1, 30, 200)
        self._theta0_deg_win = RangeWidget(self._theta0_deg_range, self.set_theta0_deg, 'AoA', "counter_slider", float)
        self.top_grid_layout.addWidget(self._theta0_deg_win)
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            pspectrum_length,
            0,
            180.0/pspectrum_length,
            "angle (in degrees)",
            "Pseudo-Spectrum (dB)",
            "",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.05)
        self.qtgui_vector_sink_f_0.set_y_axis(-50, 0)
        self.qtgui_vector_sink_f_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0.enable_grid(True)
        self.qtgui_vector_sink_f_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0.set_ref_level(0)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [2, 1, 1, 1, 1,
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
        self.tab_layout_0.addWidget(self._qtgui_vector_sink_f_0_win)
        self.qtgui_number_sink_1 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_1.set_update_time(0.10)
        self.qtgui_number_sink_1.set_title("")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_1.set_min(i, -1)
            self.qtgui_number_sink_1.set_max(i, 1)
            self.qtgui_number_sink_1.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_1.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_1.set_label(i, labels[i])
            self.qtgui_number_sink_1.set_unit(i, units[i])
            self.qtgui_number_sink_1.set_factor(i, factor[i])

        self.qtgui_number_sink_1.enable_autoscale(False)
        self._qtgui_number_sink_1_win = sip.wrapinstance(self.qtgui_number_sink_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_1_win)
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
        self.blocks_vector_to_streams_0 = blocks.vector_to_streams(gr.sizeof_float*1, num_targets)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, sample_rate,True)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*num_targets)
        self.blocks_multiply_matrix_xx_0 = blocks.multiply_matrix_cc(array_manifold_matrix, gr.TPP_ALL_TO_ALL)
        self.blocks_add_xx_0_0 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.aoa_autocorrelate_0 = aoa.correlate(num_array_elements, snapshot_size, overlap_size, 1)
        self.aoa_MUSIC_lin_array_0 = aoa.MUSIC_lin_array(norm_spacing, num_targets, num_array_elements, pspectrum_length)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(sample_rate, analog.GR_COS_WAVE, tone_freq_2, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(sample_rate, analog.GR_COS_WAVE, 10000, 1, 0, 0)
        self.analog_noise_source_x_0_0_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 0.5, 0)
        self.analog_noise_source_x_0_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 0.0005, 0)
        self.CARES_find_local_max_0 = CARES.find_local_max(num_targets, pspectrum_length, 0.0, 180.0)
        self.CARES_antenna_correction_0 = CARES.antenna_correction(num_array_elements, '/home/rtp/rtp/GNU-Radio/gr-CARES/calibration_lin_array_simulated.cfg')



        ##################################################
        # Connections
        ##################################################
        self.connect((self.CARES_antenna_correction_0, 0), (self.aoa_autocorrelate_0, 0))
        self.connect((self.CARES_antenna_correction_0, 1), (self.aoa_autocorrelate_0, 1))
        self.connect((self.CARES_antenna_correction_0, 2), (self.aoa_autocorrelate_0, 2))
        self.connect((self.CARES_antenna_correction_0, 3), (self.aoa_autocorrelate_0, 3))
        self.connect((self.CARES_find_local_max_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.CARES_find_local_max_0, 1), (self.blocks_vector_to_streams_0, 0))
        self.connect((self.analog_noise_source_x_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_noise_source_x_0_0_0, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.aoa_MUSIC_lin_array_0, 0), (self.CARES_find_local_max_0, 0))
        self.connect((self.aoa_MUSIC_lin_array_0, 0), (self.qtgui_vector_sink_f_0, 0))
        self.connect((self.aoa_autocorrelate_0, 0), (self.aoa_MUSIC_lin_array_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_matrix_xx_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.blocks_multiply_matrix_xx_0, 0), (self.CARES_antenna_correction_0, 0))
        self.connect((self.blocks_multiply_matrix_xx_0, 2), (self.CARES_antenna_correction_0, 2))
        self.connect((self.blocks_multiply_matrix_xx_0, 1), (self.CARES_antenna_correction_0, 1))
        self.connect((self.blocks_multiply_matrix_xx_0, 3), (self.CARES_antenna_correction_0, 3))
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_multiply_matrix_xx_0, 1))
        self.connect((self.blocks_vector_to_streams_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blocks_vector_to_streams_0, 1), (self.qtgui_number_sink_1, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "run_MUSIC_calib_lin_array_simulation")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_theta1_deg(self):
        return self.theta1_deg

    def set_theta1_deg(self, theta1_deg):
        self.theta1_deg = theta1_deg
        self.set_theta1(numpy.pi*self.theta1_deg/180)

    def get_theta0_deg(self):
        return self.theta0_deg

    def set_theta0_deg(self, theta0_deg):
        self.theta0_deg = theta0_deg
        self.set_theta0(numpy.pi*self.theta0_deg/180)

    def get_num_array_elements(self):
        return self.num_array_elements

    def set_num_array_elements(self, num_array_elements):
        self.num_array_elements = num_array_elements
        self.set_ant_locs(numpy.dot(0.5, numpy.arange(self.num_array_elements/2, -self.num_array_elements/2, -1) if (self.num_array_elements%2==1) else numpy.arange(self.num_array_elements/2-0.5, -self.num_array_elements/2-0.5, -1)))

    def get_theta1(self):
        return self.theta1

    def set_theta1(self, theta1):
        self.theta1 = theta1
        self.set_amv1_true(numpy.exp(-1j*self.ant_locs*2*numpy.pi*numpy.cos(self.theta1)))

    def get_theta0(self):
        return self.theta0

    def set_theta0(self, theta0):
        self.theta0 = theta0
        self.set_amv0_true(numpy.exp(-1j*self.ant_locs*2*numpy.pi*numpy.cos(self.theta0)))

    def get_ant_phases(self):
        return self.ant_phases

    def set_ant_phases(self, ant_phases):
        self.ant_phases = ant_phases
        self.set_ant_coeffs(self.ant_gains*numpy.exp(1j*self.ant_phases))

    def get_ant_locs(self):
        return self.ant_locs

    def set_ant_locs(self, ant_locs):
        self.ant_locs = ant_locs
        self.set_amv0_true(numpy.exp(-1j*self.ant_locs*2*numpy.pi*numpy.cos(self.theta0)))
        self.set_amv1_true(numpy.exp(-1j*self.ant_locs*2*numpy.pi*numpy.cos(self.theta1)))

    def get_ant_gains(self):
        return self.ant_gains

    def set_ant_gains(self, ant_gains):
        self.ant_gains = ant_gains
        self.set_ant_coeffs(self.ant_gains*numpy.exp(1j*self.ant_phases))

    def get_ant_coeffs(self):
        return self.ant_coeffs

    def set_ant_coeffs(self, ant_coeffs):
        self.ant_coeffs = ant_coeffs
        self.set_amv0(numpy.multiply(self.ant_coeffs, self.amv0_true))
        self.set_amv1(numpy.multiply(self.ant_coeffs, self.amv1_true))

    def get_amv1_true(self):
        return self.amv1_true

    def set_amv1_true(self, amv1_true):
        self.amv1_true = amv1_true
        self.set_amv1(numpy.multiply(self.ant_coeffs, self.amv1_true))

    def get_amv0_true(self):
        return self.amv0_true

    def set_amv0_true(self, amv0_true):
        self.amv0_true = amv0_true
        self.set_amv0(numpy.multiply(self.ant_coeffs, self.amv0_true))

    def get_directory_config_files(self):
        return self.directory_config_files

    def set_directory_config_files(self, directory_config_files):
        self.directory_config_files = directory_config_files
        self.set_antenna_calibration_file_name(os.path.join(self.directory_config_files, self.antenna_calibration))

    def get_antenna_calibration(self):
        return self.antenna_calibration

    def set_antenna_calibration(self, antenna_calibration):
        self.antenna_calibration = antenna_calibration
        self.set_antenna_calibration_file_name(os.path.join(self.directory_config_files, self.antenna_calibration))

    def get_amv1(self):
        return self.amv1

    def set_amv1(self, amv1):
        self.amv1 = amv1
        self.set_array_manifold_matrix(numpy.array([self.amv0, self.amv1]).transpose())

    def get_amv0(self):
        return self.amv0

    def set_amv0(self, amv0):
        self.amv0 = amv0
        self.set_array_manifold_matrix(numpy.array([self.amv0, self.amv1]).transpose())

    def get_tone_freq_2(self):
        return self.tone_freq_2

    def set_tone_freq_2(self, tone_freq_2):
        self.tone_freq_2 = tone_freq_2
        self.analog_sig_source_x_0_0.set_frequency(self.tone_freq_2)

    def get_tone_freq_1(self):
        return self.tone_freq_1

    def set_tone_freq_1(self, tone_freq_1):
        self.tone_freq_1 = tone_freq_1

    def get_snapshot_size(self):
        return self.snapshot_size

    def set_snapshot_size(self, snapshot_size):
        self.snapshot_size = snapshot_size

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.sample_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.sample_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.sample_rate)

    def get_pspectrum_length(self):
        return self.pspectrum_length

    def set_pspectrum_length(self, pspectrum_length):
        self.pspectrum_length = pspectrum_length
        self.qtgui_vector_sink_f_0.set_x_axis(0, 180.0/self.pspectrum_length)

    def get_overlap_size(self):
        return self.overlap_size

    def set_overlap_size(self, overlap_size):
        self.overlap_size = overlap_size

    def get_num_targets(self):
        return self.num_targets

    def set_num_targets(self, num_targets):
        self.num_targets = num_targets

    def get_norm_spacing(self):
        return self.norm_spacing

    def set_norm_spacing(self, norm_spacing):
        self.norm_spacing = norm_spacing

    def get_input_variables(self):
        return self.input_variables

    def set_input_variables(self, input_variables):
        self.input_variables = input_variables

    def get_array_manifold_matrix(self):
        return self.array_manifold_matrix

    def set_array_manifold_matrix(self, array_manifold_matrix):
        self.array_manifold_matrix = array_manifold_matrix
        self.blocks_multiply_matrix_xx_0.set_A(self.array_manifold_matrix)

    def get_antenna_calibration_file_name(self):
        return self.antenna_calibration_file_name

    def set_antenna_calibration_file_name(self, antenna_calibration_file_name):
        self.antenna_calibration_file_name = antenna_calibration_file_name





def main(top_block_cls=run_MUSIC_calib_lin_array_simulation, options=None):

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
