# Install script for directory: /home/rtp/rtp/GNU-Radio/gr-CARES/grc

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gnuradio/grc/blocks" TYPE FILE FILES
    "/home/rtp/rtp/GNU-Radio/gr-CARES/grc/CARES_heatmap_sink_f.block.yml"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/grc/CARES_find_local_max.block.yml"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/grc/CARES_average_and_save.block.yml"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/grc/CARES_findmax_and_save.block.yml"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/grc/CARES_phase_correct_hier.block.yml"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/grc/CARES_save_antenna_calib.block.yml"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/grc/CARES_twinrx_phase_offset_est.block.yml"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/grc/CARES_antenna_correction.block.yml"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/grc/CARES_calibrate_lin_array.block.yml"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/grc/CARES_MUSIC_lin_array.block.yml"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/grc/CARES_correlate.block.yml"
    )
endif()

