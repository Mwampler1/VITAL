#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: IIO_FMCOMMS5_find_doa_with_anetenna_calibration
# Description: From doa: run_MUSIC_lin_array_X310_TwinRX
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
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import CARES
import iio
import os

from gnuradio import qtgui

class IIO_FMCOMMS5_find_doa_with_anetenna_calibration(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "IIO_FMCOMMS5_find_doa_with_anetenna_calibration")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("IIO_FMCOMMS5_find_doa_with_anetenna_calibration")
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

        self.settings = Qt.QSettings("GNU Radio", "IIO_FMCOMMS5_find_doa_with_anetenna_calibration")

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
        self.relative_phase_offset_files = relative_phase_offset_files = "IIO_FMCOMMS5_relative_phase_offsets.txt"
        self.directory_config_files = directory_config_files = "/home/rtp/rtp/GNU-Radio/gr-CARES/apps/IIO_FMCOMMS5/"
        self.antenna_calibration = antenna_calibration = "IIO_FMCOMMS5_antenna_calibration.cfg"
        self.snapshot_size = snapshot_size = 2048
        self.rel_phase_offsets_file_name = rel_phase_offsets_file_name = os.path.join(directory_config_files, relative_phase_offset_files)
        self.pspectrum_length = pspectrum_length = 1024
        self.overlap_size = overlap_size = 512
        self.num_targets = num_targets = 1
        self.num_array_elements = num_array_elements = 4
        self.norm_spacing = norm_spacing = 0.500
        self.input_variables = input_variables = struct({

            'ToneFreq': 10000,

            'SampleRate': 10000000,

            'CenterFreq': 2450000000,

            'RxAddr': "ip:192.168.3.2",

            'Gain': 60,

            'NumArrayElements': 4,

            'NormSpacing': 0.5,

            'SnapshotSize': 2**11,

            'OverlapSize': 2**9,

            'NumTargets': 1,

            'PSpectrumLength': 2**10,

            'DirectoryConfigFiles': "/tmp",

            'RelativePhaseOffsets': "measure_X310_TwinRX_relative_phase_offsets_245.cfg",







        })
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
        self.tab.addTab(self.tab_widget_1, 'Angle of Arrival (MUSIC)')
        self.top_grid_layout.addWidget(self.tab)
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            pspectrum_length,
            0,
            180/pspectrum_length,
            "angle (in degrees)",
            "Pseudo-Spectrum (dB)",
            "vertical",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.05)
        self.qtgui_vector_sink_f_0.set_y_axis(-20, 0)
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
        self.iio_device_source_0 = iio.device_source("10.23.23.44", "cf-ad9361-A", ["voltage0","voltage1", "voltage2", "voltage3", "voltage4", "voltage5", "voltage6", "voltage7"], "ad9361-phy", [], 32768, 1 - 1)
        self.blocks_short_to_float_0_2 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0_1_0_0 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0_1_0 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0_1 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0_0_1 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0_0_0 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0_0 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*num_targets)
        self.blocks_float_to_complex_0_0_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_float*1, '/home/rtp/rtp/GNU-Radio/gr-CARES/apps/IIO_FMCOMMS5/degreeshoriz', False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.CARES_phase_correct_hier_0 = CARES.phase_correct_hier(num_array_elements, rel_phase_offsets_file_name)
        self.CARES_find_local_max_0 = CARES.find_local_max(num_targets, pspectrum_length, 0.0, 180.0)
        self.CARES_autocorrelate_0 = CARES.correlate(num_array_elements, snapshot_size, overlap_size, 1)
        self.CARES_antenna_correction_0 = CARES.antenna_correction(num_array_elements, antenna_calibration_file_name)
        self.CARES_MUSIC_lin_array_0 = CARES.MUSIC_lin_array(norm_spacing, num_targets, num_array_elements, pspectrum_length)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.CARES_MUSIC_lin_array_0, 0), (self.CARES_find_local_max_0, 0))
        self.connect((self.CARES_MUSIC_lin_array_0, 0), (self.qtgui_vector_sink_f_0, 0))
        self.connect((self.CARES_antenna_correction_0, 0), (self.CARES_autocorrelate_0, 0))
        self.connect((self.CARES_antenna_correction_0, 3), (self.CARES_autocorrelate_0, 3))
        self.connect((self.CARES_antenna_correction_0, 1), (self.CARES_autocorrelate_0, 1))
        self.connect((self.CARES_antenna_correction_0, 2), (self.CARES_autocorrelate_0, 2))
        self.connect((self.CARES_autocorrelate_0, 0), (self.CARES_MUSIC_lin_array_0, 0))
        self.connect((self.CARES_find_local_max_0, 1), (self.blocks_file_sink_0_0, 0))
        self.connect((self.CARES_find_local_max_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.CARES_find_local_max_0, 1), (self.qtgui_number_sink_0, 0))
        self.connect((self.CARES_phase_correct_hier_0, 1), (self.CARES_antenna_correction_0, 1))
        self.connect((self.CARES_phase_correct_hier_0, 2), (self.CARES_antenna_correction_0, 2))
        self.connect((self.CARES_phase_correct_hier_0, 3), (self.CARES_antenna_correction_0, 3))
        self.connect((self.CARES_phase_correct_hier_0, 0), (self.CARES_antenna_correction_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.CARES_phase_correct_hier_0, 0))
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.CARES_phase_correct_hier_0, 1))
        self.connect((self.blocks_float_to_complex_0_0_0, 0), (self.CARES_phase_correct_hier_0, 2))
        self.connect((self.blocks_float_to_complex_0_0_0_0, 0), (self.CARES_phase_correct_hier_0, 3))
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_short_to_float_0_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_short_to_float_0_0_0, 0), (self.blocks_float_to_complex_0_0, 1))
        self.connect((self.blocks_short_to_float_0_0_1, 0), (self.blocks_float_to_complex_0_0_0, 1))
        self.connect((self.blocks_short_to_float_0_1, 0), (self.blocks_float_to_complex_0_0, 0))
        self.connect((self.blocks_short_to_float_0_1_0, 0), (self.blocks_float_to_complex_0_0_0_0, 0))
        self.connect((self.blocks_short_to_float_0_1_0_0, 0), (self.blocks_float_to_complex_0_0_0_0, 1))
        self.connect((self.blocks_short_to_float_0_2, 0), (self.blocks_float_to_complex_0_0_0, 0))
        self.connect((self.iio_device_source_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.iio_device_source_0, 1), (self.blocks_short_to_float_0_0, 0))
        self.connect((self.iio_device_source_0, 3), (self.blocks_short_to_float_0_0_0, 0))
        self.connect((self.iio_device_source_0, 5), (self.blocks_short_to_float_0_0_1, 0))
        self.connect((self.iio_device_source_0, 2), (self.blocks_short_to_float_0_1, 0))
        self.connect((self.iio_device_source_0, 6), (self.blocks_short_to_float_0_1_0, 0))
        self.connect((self.iio_device_source_0, 7), (self.blocks_short_to_float_0_1_0_0, 0))
        self.connect((self.iio_device_source_0, 4), (self.blocks_short_to_float_0_2, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "IIO_FMCOMMS5_find_doa_with_anetenna_calibration")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_relative_phase_offset_files(self):
        return self.relative_phase_offset_files

    def set_relative_phase_offset_files(self, relative_phase_offset_files):
        self.relative_phase_offset_files = relative_phase_offset_files
        self.set_rel_phase_offsets_file_name(os.path.join(self.directory_config_files, self.relative_phase_offset_files))

    def get_directory_config_files(self):
        return self.directory_config_files

    def set_directory_config_files(self, directory_config_files):
        self.directory_config_files = directory_config_files
        self.set_antenna_calibration_file_name(os.path.join(self.directory_config_files, self.antenna_calibration))
        self.set_rel_phase_offsets_file_name(os.path.join(self.directory_config_files, self.relative_phase_offset_files))

    def get_antenna_calibration(self):
        return self.antenna_calibration

    def set_antenna_calibration(self, antenna_calibration):
        self.antenna_calibration = antenna_calibration
        self.set_antenna_calibration_file_name(os.path.join(self.directory_config_files, self.antenna_calibration))

    def get_snapshot_size(self):
        return self.snapshot_size

    def set_snapshot_size(self, snapshot_size):
        self.snapshot_size = snapshot_size

    def get_rel_phase_offsets_file_name(self):
        return self.rel_phase_offsets_file_name

    def set_rel_phase_offsets_file_name(self, rel_phase_offsets_file_name):
        self.rel_phase_offsets_file_name = rel_phase_offsets_file_name

    def get_pspectrum_length(self):
        return self.pspectrum_length

    def set_pspectrum_length(self, pspectrum_length):
        self.pspectrum_length = pspectrum_length
        self.qtgui_vector_sink_f_0.set_x_axis(0, 180/self.pspectrum_length)

    def get_overlap_size(self):
        return self.overlap_size

    def set_overlap_size(self, overlap_size):
        self.overlap_size = overlap_size

    def get_num_targets(self):
        return self.num_targets

    def set_num_targets(self, num_targets):
        self.num_targets = num_targets

    def get_num_array_elements(self):
        return self.num_array_elements

    def set_num_array_elements(self, num_array_elements):
        self.num_array_elements = num_array_elements

    def get_norm_spacing(self):
        return self.norm_spacing

    def set_norm_spacing(self, norm_spacing):
        self.norm_spacing = norm_spacing

    def get_input_variables(self):
        return self.input_variables

    def set_input_variables(self, input_variables):
        self.input_variables = input_variables

    def get_antenna_calibration_file_name(self):
        return self.antenna_calibration_file_name

    def set_antenna_calibration_file_name(self, antenna_calibration_file_name):
        self.antenna_calibration_file_name = antenna_calibration_file_name





def main(top_block_cls=IIO_FMCOMMS5_find_doa_with_anetenna_calibration, options=None):

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
