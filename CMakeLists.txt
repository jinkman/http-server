# 最低指定的CMake版本
cmake_minimum_required(VERSION 3.0)

# 括号里面填你的工程名
set(PRO_NAME "http-server")
PROJECT(PRO_NAME)

set(CMAKE_CXX_STANDARD 17)

add_compile_options(-Wno-nonportable-include-path)

# 设置输出路径
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# 三方库路径
set(third-party-path ${CMAKE_CURRENT_SOURCE_DIR}/third-party)

# Data路径
set(data-path ${CMAKE_CURRENT_SOURCE_DIR}/data)
set(DATA_PATH ${data-path}/)

# 添加三方库

set(SRC_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src)
# 添加头文件
list(APPEND INCLUDES_DIR ${SRC_DIR}/)
list(APPEND INCLUDES_DIR ${third-party-path}/cpp-httplib)

# 配置文件
# configure_file(
#     "${SRC_DIR}/common/Config.h.in"
#     "${SRC_DIR}/common/Config.h"
# )

# 遍历源代码文件，构建工程
file(GLOB_RECURSE SRC_CPP ${SRC_DIR}/*.cpp ${SRC_DIR}/*.c)
file(GLOB_RECURSE SRC_H ${SRC_DIR}/*.h ${SRC_DIR}/*.hpp)

add_executable(${PRO_NAME}
    ${SRC_CPP}
    ${SRC_H}
)

target_include_directories(${PRO_NAME}
    PUBLIC
    ${INCLUDES_DIR}
)