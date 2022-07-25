INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_CARES CARES)

FIND_PATH(
    CARES_INCLUDE_DIRS
    NAMES CARES/api.h
    HINTS $ENV{CARES_DIR}/include
        ${PC_CARES_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    CARES_LIBRARIES
    NAMES gnuradio-CARES
    HINTS $ENV{CARES_DIR}/lib
        ${PC_CARES_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/CARESTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(CARES DEFAULT_MSG CARES_LIBRARIES CARES_INCLUDE_DIRS)
MARK_AS_ADVANCED(CARES_LIBRARIES CARES_INCLUDE_DIRS)
