#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Run Calib Lin Array Simulation
# GNU Radio version: 3.8.2.0

def struct(data): return type('Struct', (object,), data)()
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
import os


class run_calib_lin_array_simulation(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Run Calib Lin Array Simulation")

        ##################################################
        # Variables
        ##################################################
        self.pilot_angle_degrees = pilot_angle_degrees = 30
        self.num_array_elements = num_array_elements = 4
        self.input_variables = input_variables = struct({

            'SampleRate': 3200000,

            'ToneFreq1': 10000,

            'ToneFreq2': 20000,

            'NormSpacing': 0.5,

            'NumArrayElements': 4,

            'PSpectrumLength': 2**10,

            'SnapshotSize': 2**11,

            'OverlapSize': 2**9,

            'AntGains': numpy.array([ 0.94984789,  0.4544107 ,  0.34649469,  0.25083929]),

            'AntPhases': numpy.array([ 0.28647672,  5.27248071,  2.71271102,  1.36970886]),

            'PilotAngleDegrees': 30.0,

            'DirectoryConfigFiles': "/tmp",

            'AntennaCalibration': "calibration_lin_array_simulated.cfg",

            'Samples2Avg': 2**11,






        })
        self.pilot_theta0 = pilot_theta0 = numpy.pi*pilot_angle_degrees/180
        self.ant_phases = ant_phases = numpy.array([ 0.28647672,  5.27248071,  2.71271102,  1.36970886])
        self.ant_locs = ant_locs = numpy.dot(0.5, numpy.arange(num_array_elements/2, -input_variables.NumArrayElements/2, -1) if (num_array_elements%2==1) else numpy.arange(num_array_elements/2-0.5, -num_array_elements/2-0.5, -1))
        self.ant_gains = ant_gains = numpy.array([ 0.94984789,  0.4544107 ,  0.34649469,  0.25083929])
        self.ant_coeffs = ant_coeffs = ant_gains*numpy.exp(1j*ant_phases)
        self.amv0_true = amv0_true = numpy.exp(-1j*ant_locs*2*numpy.pi*numpy.cos(pilot_theta0))
        self.directory_config_files = directory_config_files = "/home/rtp/rtp/GNU-Radio/gr-CARES/examples/"
        self.antenna_calibration = antenna_calibration = "calibration_lin_array_simulated.cfg"
        self.amv0 = amv0 = numpy.multiply(ant_coeffs, amv0_true)
        self.tone_freq_2 = tone_freq_2 = 20000
        self.tone_freq_1 = tone_freq_1 = 10000
        self.snapshot_size = snapshot_size = 2048
        self.samples_2_avg = samples_2_avg = 2048
        self.sample_rate = sample_rate = 320000
        self.pspectrum_length = pspectrum_length = 1024
        self.overlap_size = overlap_size = 512
        self.num_targets = num_targets = 2
        self.norm_spacing = norm_spacing = 0.500
        self.array_manifold_matrix = array_manifold_matrix = numpy.array([amv0]).transpose()
        self.antenna_calibration_file_name = antenna_calibration_file_name = os.path.join(directory_config_files, antenna_calibration)

        ##################################################
        # Blocks
        ##################################################
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, sample_rate,True)
        self.blocks_multiply_matrix_xx_0 = blocks.multiply_matrix_cc(array_manifold_matrix, gr.TPP_ALL_TO_ALL)
        self.blocks_complex_to_magphase_0 = blocks.complex_to_magphase(num_array_elements)
        self.blocks_add_xx_0_0 = blocks.add_vcc(1)
        self.aoa_autocorrelate_0 = aoa.correlate(num_array_elements, snapshot_size, overlap_size, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(sample_rate, analog.GR_COS_WAVE, tone_freq_2, 1, 0, 0)
        self.analog_noise_source_x_0_0_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 0.5, 0)
        self.CARES_save_antenna_calib_0 = CARES.save_antenna_calib(num_array_elements, 'calibration_lin_array_simulated.cfg', samples_2_avg)
        self.CARES_calibrate_lin_array_0 = CARES.calibrate_lin_array(norm_spacing, num_array_elements, pilot_angle_degrees)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.CARES_calibrate_lin_array_0, 0), (self.blocks_complex_to_magphase_0, 0))
        self.connect((self.analog_noise_source_x_0_0_0, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.aoa_autocorrelate_0, 0), (self.CARES_calibrate_lin_array_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.blocks_complex_to_magphase_0, 1), (self.CARES_save_antenna_calib_0, 1))
        self.connect((self.blocks_complex_to_magphase_0, 0), (self.CARES_save_antenna_calib_0, 0))
        self.connect((self.blocks_multiply_matrix_xx_0, 3), (self.aoa_autocorrelate_0, 3))
        self.connect((self.blocks_multiply_matrix_xx_0, 1), (self.aoa_autocorrelate_0, 1))
        self.connect((self.blocks_multiply_matrix_xx_0, 0), (self.aoa_autocorrelate_0, 0))
        self.connect((self.blocks_multiply_matrix_xx_0, 2), (self.aoa_autocorrelate_0, 2))
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_multiply_matrix_xx_0, 0))


    def get_pilot_angle_degrees(self):
        return self.pilot_angle_degrees

    def set_pilot_angle_degrees(self, pilot_angle_degrees):
        self.pilot_angle_degrees = pilot_angle_degrees
        self.set_pilot_theta0(numpy.pi*self.pilot_angle_degrees/180)

    def get_num_array_elements(self):
        return self.num_array_elements

    def set_num_array_elements(self, num_array_elements):
        self.num_array_elements = num_array_elements
        self.set_ant_locs(numpy.dot(0.5, numpy.arange(self.num_array_elements/2, -input_variables.NumArrayElements/2, -1) if (self.num_array_elements%2==1) else numpy.arange(self.num_array_elements/2-0.5, -self.num_array_elements/2-0.5, -1)))

    def get_input_variables(self):
        return self.input_variables

    def set_input_variables(self, input_variables):
        self.input_variables = input_variables

    def get_pilot_theta0(self):
        return self.pilot_theta0

    def set_pilot_theta0(self, pilot_theta0):
        self.pilot_theta0 = pilot_theta0
        self.set_amv0_true(numpy.exp(-1j*self.ant_locs*2*numpy.pi*numpy.cos(self.pilot_theta0)))

    def get_ant_phases(self):
        return self.ant_phases

    def set_ant_phases(self, ant_phases):
        self.ant_phases = ant_phases
        self.set_ant_coeffs(self.ant_gains*numpy.exp(1j*self.ant_phases))

    def get_ant_locs(self):
        return self.ant_locs

    def set_ant_locs(self, ant_locs):
        self.ant_locs = ant_locs
        self.set_amv0_true(numpy.exp(-1j*self.ant_locs*2*numpy.pi*numpy.cos(self.pilot_theta0)))

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

    def get_amv0(self):
        return self.amv0

    def set_amv0(self, amv0):
        self.amv0 = amv0
        self.set_array_manifold_matrix(numpy.array([self.amv0]).transpose())

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

    def get_samples_2_avg(self):
        return self.samples_2_avg

    def set_samples_2_avg(self, samples_2_avg):
        self.samples_2_avg = samples_2_avg

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self.analog_sig_source_x_0_0.set_sampling_freq(self.sample_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.sample_rate)

    def get_pspectrum_length(self):
        return self.pspectrum_length

    def set_pspectrum_length(self, pspectrum_length):
        self.pspectrum_length = pspectrum_length

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

    def get_array_manifold_matrix(self):
        return self.array_manifold_matrix

    def set_array_manifold_matrix(self, array_manifold_matrix):
        self.array_manifold_matrix = array_manifold_matrix
        self.blocks_multiply_matrix_xx_0.set_A(self.array_manifold_matrix)

    def get_antenna_calibration_file_name(self):
        return self.antenna_calibration_file_name

    def set_antenna_calibration_file_name(self, antenna_calibration_file_name):
        self.antenna_calibration_file_name = antenna_calibration_file_name





def main(top_block_cls=run_calib_lin_array_simulation, options=None):
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
