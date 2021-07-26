# Automatically generated by scripts/boost/generate-ports.ps1

vcpkg_from_github(
    OUT_SOURCE_PATH SOURCE_PATH
    REPO boostorg/assign
    REF boost-1.75.0
    SHA512 33c5adc9fe35b670ab9be1e68d61970e6c1ea0a870791fd446669cf501e665e615e72da5bb50a61e0e6bc6d7e695513d1bf73e91f845c5d1b47e694868da2baf
    HEAD_REF master
)

include(${CURRENT_INSTALLED_DIR}/share/boost-vcpkg-helpers/boost-modular-headers.cmake)
boost_modular_headers(SOURCE_PATH ${SOURCE_PATH})