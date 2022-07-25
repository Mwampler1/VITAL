#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Estimate X310 Twinrx Constant Phase Offsets And Save
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

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import CARES
import iio
import os

from gnuradio import qtgui

class estimate_X310_TwinRX_constant_phase_offsets_and_save(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Estimate X310 Twinrx Constant Phase Offsets And Save")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Estimate X310 Twinrx Constant Phase Offsets And Save")
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

        self.settings = Qt.QSettings("GNU Radio", "estimate_X310_TwinRX_constant_phase_offsets_and_save")

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
        self.relative_phase_offset_files = relative_phase_offset_files = "FMCOMMS5_relative_phase_offsets.cfg"
        self.directory_config_files = directory_config_files = "/tmp"
        self.tone_freq = tone_freq = 10000
        self.skip_ahead = skip_ahead = 32768
        self.samples_2_find_max = samples_2_find_max = 2048
        self.samp_rate = samp_rate = 10000000
        self.rx_addr = rx_addr = "addr=192.168.10.2"
        self.rel_phase_offsets_file_name = rel_phase_offsets_file_name = os.path.join(directory_config_files, relative_phase_offset_files)
        self.num_array_elements = num_array_elements = 4
        self.gain = gain = 60
        self.center_freq = center_freq = 2450000000

        ##################################################
        # Blocks
        ##################################################
        self.iio_fmcomms5_source_0 = iio.fmcomms5_source_f32c("10.23.23.40", center_freq, center_freq, samp_rate, samp_rate, True, True, True, True, 0x8000, True, True, True, 'manual', gain, 'manual', gain, 'manual', gain, 'manual', gain, 'A_BALANCED', '')
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1, "IIO_FMCOMMS5_relative_phase_offsets.cfg", False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.CARES_twinrx_phase_offset_est_0 = CARES.twinrx_phase_offset_est(num_array_elements, skip_ahead)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.CARES_twinrx_phase_offset_est_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.CARES_twinrx_phase_offset_est_0, 1), (self.blocks_null_sink_0, 0))
        self.connect((self.CARES_twinrx_phase_offset_est_0, 2), (self.blocks_null_sink_0_0, 0))
        self.connect((self.iio_fmcomms5_source_0, 1), (self.CARES_twinrx_phase_offset_est_0, 1))
        self.connect((self.iio_fmcomms5_source_0, 2), (self.CARES_twinrx_phase_offset_est_0, 2))
        self.connect((self.iio_fmcomms5_source_0, 3), (self.CARES_twinrx_phase_offset_est_0, 3))
        self.connect((self.iio_fmcomms5_source_0, 0), (self.CARES_twinrx_phase_offset_est_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "estimate_X310_TwinRX_constant_phase_offsets_and_save")
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

    def get_tone_freq(self):
        return self.tone_freq

    def set_tone_freq(self, tone_freq):
        self.tone_freq = tone_freq

    def get_skip_ahead(self):
        return self.skip_ahead

    def set_skip_ahead(self, skip_ahead):
        self.skip_ahead = skip_ahead

    def get_samples_2_find_max(self):
        return self.samples_2_find_max

    def set_samples_2_find_max(self, samples_2_find_max):
        self.samples_2_find_max = samples_2_find_max

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.iio_fmcomms5_source_0.set_params(self.center_freq, self.center_freq, self.samp_rate, self.samp_rate, True, True, True, 'manual', self.gain, 'manual', self.gain, 'manual', self.gain, 'manual', self.gain, 'A_BALANCED')

    def get_rx_addr(self):
        return self.rx_addr

    def set_rx_addr(self, rx_addr):
        self.rx_addr = rx_addr

    def get_rel_phase_offsets_file_name(self):
        return self.rel_phase_offsets_file_name

    def set_rel_phase_offsets_file_name(self, rel_phase_offsets_file_name):
        self.rel_phase_offsets_file_name = rel_phase_offsets_file_name

    def get_num_array_elements(self):
        return self.num_array_elements

    def set_num_array_elements(self, num_array_elements):
        self.num_array_elements = num_array_elements

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.iio_fmcomms5_source_0.set_params(self.center_freq, self.center_freq, self.samp_rate, self.samp_rate, True, True, True, 'manual', self.gain, 'manual', self.gain, 'manual', self.gain, 'manual', self.gain, 'A_BALANCED')

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.iio_fmcomms5_source_0.set_params(self.center_freq, self.center_freq, self.samp_rate, self.samp_rate, True, True, True, 'manual', self.gain, 'manual', self.gain, 'manual', self.gain, 'manual', self.gain, 'A_BALANCED')





def main(top_block_cls=estimate_X310_TwinRX_constant_phase_offsets_and_save, options=None):

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
