/* -*- c++ -*- */

#define CARES_API

%include "gnuradio.i"           // the common stuff

//load generated python docstrings
%include "CARES_swig_doc.i"

%{
#include "CARES/find_local_max.h"
#include "CARES/antenna_correction.h"
#include "CARES/calibrate_lin_array.h"
#include "CARES/MUSIC_lin_array.h"
#include "CARES/correlate.h"
%}

%include "CARES/find_local_max.h"
GR_SWIG_BLOCK_MAGIC2(CARES, find_local_max);
%include "CARES/antenna_correction.h"
GR_SWIG_BLOCK_MAGIC2(CARES, antenna_correction);
%include "CARES/calibrate_lin_array.h"
GR_SWIG_BLOCK_MAGIC2(CARES, calibrate_lin_array);
%include "CARES/MUSIC_lin_array.h"
GR_SWIG_BLOCK_MAGIC2(CARES, MUSIC_lin_array);
%include "CARES/correlate.h"
GR_SWIG_BLOCK_MAGIC2(CARES, correlate);

