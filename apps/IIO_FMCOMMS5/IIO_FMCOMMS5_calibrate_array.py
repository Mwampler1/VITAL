#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: IIO_FMCOMMS5_calibrate_array
# Description: From doa: calibrate_lin_array_X310_TwinRX
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


class IIO_FMCOMMS5_calibrate_array(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "IIO_FMCOMMS5_calibrate_array")

        ##################################################
        # Variables
        ##################################################
        self.relative_phase_offset_files = relative_phase_offset_files = "IIO_FMCOMMS5_relative_phase_offsets.txt"
        self.directory_config_files = directory_config_files = "/home/rtp/rtp/GNU-Radio/gr-CARES/apps/IIO_FMCOMMS5/"
        self.antenna_calibration = antenna_calibration = "IIO_FMCOMMS5_antenna_calibration.cfg"
        self.snapshot_size = snapshot_size = 2048
        self.samples_2_avg = samples_2_avg = 2048
        self.rel_phase_offsets_file_name = rel_phase_offsets_file_name = os.path.join(directory_config_files, relative_phase_offset_files)
        self.pilot_angle = pilot_angle = 90
        self.overlap_size = overlap_size = 512
        self.num_array_elements = num_array_elements = 4
        self.norm_spacing = norm_spacing = 0.500
        self.antenna_calibration_file_name = antenna_calibration_file_name = os.path.join(directory_config_files, antenna_calibration)

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
        self.blocks_complex_to_magphase_0 = blocks.complex_to_magphase(num_array_elements)
        self.CARES_save_antenna_calib_0 = CARES.save_antenna_calib(num_array_elements, antenna_calibration_file_name, samples_2_avg)
        self.CARES_phase_correct_hier_0 = CARES.phase_correct_hier(num_array_elements, rel_phase_offsets_file_name)
        self.CARES_calibrate_lin_array_0 = CARES.calibrate_lin_array(norm_spacing, num_array_elements, pilot_angle)
        self.CARES_autocorrelate_0 = CARES.correlate(num_array_elements, snapshot_size, overlap_size, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.CARES_autocorrelate_0, 0), (self.CARES_calibrate_lin_array_0, 0))
        self.connect((self.CARES_calibrate_lin_array_0, 0), (self.blocks_complex_to_magphase_0, 0))
        self.connect((self.CARES_phase_correct_hier_0, 0), (self.CARES_autocorrelate_0, 0))
        self.connect((self.CARES_phase_correct_hier_0, 1), (self.CARES_autocorrelate_0, 1))
        self.connect((self.CARES_phase_correct_hier_0, 3), (self.CARES_autocorrelate_0, 3))
        self.connect((self.CARES_phase_correct_hier_0, 2), (self.CARES_autocorrelate_0, 2))
        self.connect((self.blocks_complex_to_magphase_0, 0), (self.CARES_save_antenna_calib_0, 0))
        self.connect((self.blocks_complex_to_magphase_0, 1), (self.CARES_save_antenna_calib_0, 1))
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

    def get_samples_2_avg(self):
        return self.samples_2_avg

    def set_samples_2_avg(self, samples_2_avg):
        self.samples_2_avg = samples_2_avg

    def get_rel_phase_offsets_file_name(self):
        return self.rel_phase_offsets_file_name

    def set_rel_phase_offsets_file_name(self, rel_phase_offsets_file_name):
        self.rel_phase_offsets_file_name = rel_phase_offsets_file_name

    def get_pilot_angle(self):
        return self.pilot_angle

    def set_pilot_angle(self, pilot_angle):
        self.pilot_angle = pilot_angle

    def get_overlap_size(self):
        return self.overlap_size

    def set_overlap_size(self, overlap_size):
        self.overlap_size = overlap_size

    def get_num_array_elements(self):
        return self.num_array_elements

    def set_num_array_elements(self, num_array_elements):
        self.num_array_elements = num_array_elements

    def get_norm_spacing(self):
        return self.norm_spacing

    def set_norm_spacing(self, norm_spacing):
        self.norm_spacing = norm_spacing

    def get_antenna_calibration_file_name(self):
        return self.antenna_calibration_file_name

    def set_antenna_calibration_file_name(self, antenna_calibration_file_name):
        self.antenna_calibration_file_name = antenna_calibration_file_name





def main(top_block_cls=IIO_FMCOMMS5_calibrate_array, options=None):
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
