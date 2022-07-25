# Install script for directory: /home/rtp/rtp/GNU-Radio/gr-CARES/python

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/CARES" TYPE FILE FILES
    "/home/rtp/rtp/GNU-Radio/gr-CARES/python/__init__.py"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/python/heatmap_sink_f.py"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/python/average_and_save.py"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/python/findmax_and_save.py"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/python/phase_correct_hier.py"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/python/save_antenna_calib.py"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/python/twinrx_phase_offset_est.py"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/CARES" TYPE FILE FILES
    "/home/rtp/rtp/GNU-Radio/gr-CARES/build/python/__init__.pyc"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/build/python/heatmap_sink_f.pyc"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/build/python/average_and_save.pyc"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/build/python/findmax_and_save.pyc"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/build/python/phase_correct_hier.pyc"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/build/python/save_antenna_calib.pyc"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/build/python/twinrx_phase_offset_est.pyc"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/build/python/__init__.pyo"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/build/python/heatmap_sink_f.pyo"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/build/python/average_and_save.pyo"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/build/python/findmax_and_save.pyo"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/build/python/phase_correct_hier.pyo"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/build/python/save_antenna_calib.pyo"
    "/home/rtp/rtp/GNU-Radio/gr-CARES/build/python/twinrx_phase_offset_est.pyo"
    )
endif()

