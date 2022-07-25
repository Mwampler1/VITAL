#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: IIO_FMCOMMS5_calculate_phase_offset
# Description: From DOA: estimate_X310_TwinRX_constant_phase_offsets_and_save
# GNU Radio version: 3.8.2.0

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


class IIO_FMCOMMS5_calculate_phase_offset(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "IIO_FMCOMMS5_calculate_phase_offset")

        ##################################################
        # Variables
        ##################################################
        self.relative_phase_offset_files = relative_phase_offset_files = "IIO_FMCOMMS5_relative_phase_offsets_1.txt"
        self.filepath3 = filepath3 = "/home/rtp/rtp/GNU-Radio/gr-CARES/apps/IIO_FMCOMMS5/"
        self.filepath2 = filepath2 = "/home/rtp/rtp/GNU-Radio/gr-CARES/apps/IIO_FMCOMMS5/"
        self.file3 = file3 = "IIO_FMCOMMS5_relative_phase_offsets_3.txt"
        self.file2 = file2 = "IIO_FMCOMMS5_relative_phase_offsets_2.txt"
        self.directory_config_files = directory_config_files = "/home/rtp/rtp/GNU-Radio/gr-CARES/apps/IIO_FMCOMMS5/"
        self.tone_freq = tone_freq = 10000
        self.skip_ahead = skip_ahead = 32768
        self.samples_2_find_max = samples_2_find_max = 2048
        self.samp_rate = samp_rate = 10000000
        self.rel_phase_offsets_file_name = rel_phase_offsets_file_name = os.path.join(directory_config_files, relative_phase_offset_files)
        self.num_array_elements = num_array_elements = 4
        self.filepathfinal3 = filepathfinal3 = os.path.join(filepath3, file3)
        self.filepathfinal2 = filepathfinal2 = os.path.join(filepath2, file2)
        self.center_freq = center_freq = 2450000000

        ##################################################
        # Blocks
        ##################################################
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
        self.CARES_twinrx_phase_offset_est_0 = CARES.twinrx_phase_offset_est(num_array_elements, skip_ahead)
        self.CARES_findmax_and_save_0_0_0_0 = CARES.findmax_and_save(samples_2_find_max, 1, filepathfinal3)
        self.CARES_findmax_and_save_0_0_0 = CARES.findmax_and_save(samples_2_find_max, 1, filepathfinal2)
        self.CARES_findmax_and_save_0_0 = CARES.findmax_and_save(samples_2_find_max, 1, rel_phase_offsets_file_name)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.CARES_twinrx_phase_offset_est_0, 0), (self.CARES_findmax_and_save_0_0, 0))
        self.connect((self.CARES_twinrx_phase_offset_est_0, 1), (self.CARES_findmax_and_save_0_0_0, 0))
        self.connect((self.CARES_twinrx_phase_offset_est_0, 2), (self.CARES_findmax_and_save_0_0_0_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.CARES_twinrx_phase_offset_est_0, 0))
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.CARES_twinrx_phase_offset_est_0, 1))
        self.connect((self.blocks_float_to_complex_0_0_0, 0), (self.CARES_twinrx_phase_offset_est_0, 2))
        self.connect((self.blocks_float_to_complex_0_0_0_0, 0), (self.CARES_twinrx_phase_offset_est_0, 3))
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


    def get_relative_phase_offset_files(self):
        return self.relative_phase_offset_files

    def set_relative_phase_offset_files(self, relative_phase_offset_files):
        self.relative_phase_offset_files = relative_phase_offset_files
        self.set_rel_phase_offsets_file_name(os.path.join(self.directory_config_files, self.relative_phase_offset_files))

    def get_filepath3(self):
        return self.filepath3

    def set_filepath3(self, filepath3):
        self.filepath3 = filepath3
        self.set_filepathfinal3(os.path.join(self.filepath3, self.file3))

    def get_filepath2(self):
        return self.filepath2

    def set_filepath2(self, filepath2):
        self.filepath2 = filepath2
        self.set_filepathfinal2(os.path.join(self.filepath2, self.file2))

    def get_file3(self):
        return self.file3

    def set_file3(self, file3):
        self.file3 = file3
        self.set_filepathfinal3(os.path.join(self.filepath3, self.file3))

    def get_file2(self):
        return self.file2

    def set_file2(self, file2):
        self.file2 = file2
        self.set_filepathfinal2(os.path.join(self.filepath2, self.file2))

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

    def get_rel_phase_offsets_file_name(self):
        return self.rel_phase_offsets_file_name

    def set_rel_phase_offsets_file_name(self, rel_phase_offsets_file_name):
        self.rel_phase_offsets_file_name = rel_phase_offsets_file_name

    def get_num_array_elements(self):
        return self.num_array_elements

    def set_num_array_elements(self, num_array_elements):
        self.num_array_elements = num_array_elements

    def get_filepathfinal3(self):
        return self.filepathfinal3

    def set_filepathfinal3(self, filepathfinal3):
        self.filepathfinal3 = filepathfinal3

    def get_filepathfinal2(self):
        return self.filepathfinal2

    def set_filepathfinal2(self, filepathfinal2):
        self.filepathfinal2 = filepathfinal2

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq





def main(top_block_cls=IIO_FMCOMMS5_calculate_phase_offset, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    tb.wait()


if __name__ == '__main__':
    main()
