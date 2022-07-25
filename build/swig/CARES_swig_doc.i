
/*
 * This file was automatically generated using swig_doc.py.
 *
 * Any changes to it will be lost next time it is regenerated.
 */




%feature("docstring") gr::CARES::antenna_correction "Performs a scaling operation on a correlation matrix.

This block takes a correlation matrix of size (number of antenna elements x number of antenna elements) as input and multiplies it with a diagonal matrix of size (number of antenna elements x number of antenna elements) using calibration values retrieved from a config file.

Constructor Specific Documentation:

Make a block to correct a correlation matrix for non-uniform antenna gain and phase.

Args:
    num_ant_ele : Number of antenna elements
    config_filename : Config file consisting of antenna calibration values"

%feature("docstring") gr::CARES::antenna_correction::make "Performs a scaling operation on a correlation matrix.

This block takes a correlation matrix of size (number of antenna elements x number of antenna elements) as input and multiplies it with a diagonal matrix of size (number of antenna elements x number of antenna elements) using calibration values retrieved from a config file.

Constructor Specific Documentation:

Make a block to correct a correlation matrix for non-uniform antenna gain and phase.

Args:
    num_ant_ele : Number of antenna elements
    config_filename : Config file consisting of antenna calibration values"

%feature("docstring") gr::CARES::calibrate_lin_array "Calibrate a linear antenna array.

This block takes a correlation matrix of size (number of antenna elements x number of antenna elements) as input and generates a complex vector of size (number of antenna elements x 1) which can be utilized to calibrate a linear array.

Constructor Specific Documentation:

Make a block to calibrate linear arrays.

Args:
    norm_spacing : Normalized spacing between antenna elements
    num_ant_ele : Number of antenna elements
    pilot_angle : Known angle of a pilot transmitter used for calibration"

%feature("docstring") gr::CARES::calibrate_lin_array::make "Calibrate a linear antenna array.

This block takes a correlation matrix of size (number of antenna elements x number of antenna elements) as input and generates a complex vector of size (number of antenna elements x 1) which can be utilized to calibrate a linear array.

Constructor Specific Documentation:

Make a block to calibrate linear arrays.

Args:
    norm_spacing : Normalized spacing between antenna elements
    num_ant_ele : Number of antenna elements
    pilot_angle : Known angle of a pilot transmitter used for calibration"

%feature("docstring") gr::CARES::correlate "Calculate autocorrelation matrix of input data snapshot.

Constructor Specific Documentation:

Make an correlate block.

Args:
    inputs : Number of input streams
    snapshot_size : Size of each snapshot
    overlap_size : Size of the overlap between successive snapshots
    avg_method : Use Forward Averaging or Forward-Backward Averaging"

%feature("docstring") gr::CARES::correlate::make "Calculate autocorrelation matrix of input data snapshot.

Constructor Specific Documentation:

Make an correlate block.

Args:
    inputs : Number of input streams
    snapshot_size : Size of each snapshot
    overlap_size : Size of the overlap between successive snapshots
    avg_method : Use Forward Averaging or Forward-Backward Averaging"

%feature("docstring") gr::CARES::find_local_max "Finds a given number of local maxima in a vector.

This block takes a vector of size (vector-length x 1) as input and outputs a float vector of size (number of max. values x 1) consisting of max. values and a float vector of size (number of max. values x 1) consisting of their locations.

Constructor Specific Documentation:

Make a block to find the local maxima and their locations.

Args:
    num_max_vals : Number of max. values
    vector_len : Length of the input vector
    x_min : Min. value of the index vector
    x_max : Max. value of the index vector"

%feature("docstring") gr::CARES::find_local_max::make "Finds a given number of local maxima in a vector.

This block takes a vector of size (vector-length x 1) as input and outputs a float vector of size (number of max. values x 1) consisting of max. values and a float vector of size (number of max. values x 1) consisting of their locations.

Constructor Specific Documentation:

Make a block to find the local maxima and their locations.

Args:
    num_max_vals : Number of max. values
    vector_len : Length of the input vector
    x_min : Min. value of the index vector
    x_max : Max. value of the index vector"

%feature("docstring") gr::CARES::MUSIC_lin_array "Performs DoA estimation using MUSIC algorithm for a linear antenna array.

This block takes a correlation matrix of size (number of antenna elements x number of antenna elements) as input and generates a complex vector of size (pseudo-spectrum length x 1) whose arg-max values represent the estimated DoAs.

Constructor Specific Documentation:

Make a block to estimate DoAs using MUSIC algorithm for linear arrays.

Args:
    norm_spacing : Normalized spacing between antenna elements
    num_targets : Known number of targets
    num_ant_ele : Number of antenna elements
    pspectrum_len : Length of the Pseudo-Spectrum length"

%feature("docstring") gr::CARES::MUSIC_lin_array::make "Performs DoA estimation using MUSIC algorithm for a linear antenna array.

This block takes a correlation matrix of size (number of antenna elements x number of antenna elements) as input and generates a complex vector of size (pseudo-spectrum length x 1) whose arg-max values represent the estimated DoAs.

Constructor Specific Documentation:

Make a block to estimate DoAs using MUSIC algorithm for linear arrays.

Args:
    norm_spacing : Normalized spacing between antenna elements
    num_targets : Known number of targets
    num_ant_ele : Number of antenna elements
    pspectrum_len : Length of the Pseudo-Spectrum length"