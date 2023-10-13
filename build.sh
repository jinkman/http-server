#!/bin/sh
workdir=$(cd $(dirname $0); pwd -P)
#git submodule update --init --recursive --progress

build_type="Release"
if [[ x"$1" == x"Debug" ]]; then
    build_type="Debug"
fi

if [[ x"$1" == x"r" ]]; then
    rm -rf ${workdir}/build
    build_type="Debug"
fi

target=""

cd ${workdir} && \
mkdir -p "$workdir/build" && cd "$workdir/build/" && \
cmake -DCMAKE_CXX_STANDARD=17 ../ && \
make -j 12

if [[ $? -ne 0 ]]; then
    echo "ERROR: Failed to build"
    exit -1
fi