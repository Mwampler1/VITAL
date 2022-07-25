#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: IIO_FMCOMMS5_view_corrected_phase_offsets
# Author: megan
# Description: From doa: view_X310_TwinRX_op_with_corrected_phase_offsets
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

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import blocks
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import CARES
import iio
import os

from gnuradio import qtgui

class IIO_FMCOMMS5_view_corrected_phase_offsets(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "IIO_FMCOMMS5_view_corrected_phase_offsets")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("IIO_FMCOMMS5_view_corrected_phase_offsets")
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

        self.settings = Qt.QSettings("GNU Radio", "IIO_FMCOMMS5_view_corrected_phase_offsets")

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
        self.samp_rate = samp_rate = 10000000
        self.rel_phase_offsets_file_name = rel_phase_offsets_file_name = os.path.join(directory_config_files, relative_phase_offset_files)

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            4 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.5)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(False)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(8):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.iio_device_source_0 = iio.device_source("10.23.23.40", "cf-ad9361-A", ["voltage0","voltage1", "voltage2", "voltage3", "voltage4", "voltage5", "voltage6", "voltage7"], "ad9361-phy", [], 32768, 1 - 1)
        self.blocks_short_to_float_0_2 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0_1_0_0 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0_1_0 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0_1 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0_0_1 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0_0_0 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0_0 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_float_to_complex_0_0_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.CARES_phase_correct_hier_0 = CARES.phase_correct_hier(4, rel_phase_offsets_file_name)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.CARES_phase_correct_hier_0, 2), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.CARES_phase_correct_hier_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.CARES_phase_correct_hier_0, 3), (self.qtgui_time_sink_x_0, 3))
        self.connect((self.CARES_phase_correct_hier_0, 1), (self.qtgui_time_sink_x_0, 1))
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
        self.settings = Qt.QSettings("GNU Radio", "IIO_FMCOMMS5_view_corrected_phase_offsets")
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
        self.set_rel_phase_offsets_file_name(os.path.join(self.directory_config_files, self.relative_phase_offset_files))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_rel_phase_offsets_file_name(self):
        return self.rel_phase_offsets_file_name

    def set_rel_phase_offsets_file_name(self, rel_phase_offsets_file_name):
        self.rel_phase_offsets_file_name = rel_phase_offsets_file_name





def main(top_block_cls=IIO_FMCOMMS5_view_corrected_phase_offsets, options=None):

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
