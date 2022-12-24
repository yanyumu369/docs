cmake_minimum_required(VERSION 3.12)
project(Sales_data VERSION 1.0.0 LANGUAGES CXX DESCRIPTION "Sales_data")

##--------------------- Version file ---------------------------------------##
configure_file(src/cmake_template_version.h.in "${PROJECT_SOURCE_DIR}/src/cmake_template_version.h")

# Specified the language standard
set(CMAKE_CXX_STANDARD 11)

##--------------------- Compile Options ------------------------------------##
# Configure compile options
add_compile_options(-Wall -Wextra -pedantic -Werror)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pipe -std=c++11")

# Set build type
# set(CMAKE_BUILD_TYPE Debug)  # Use `cmake -DCMAKE_BUILD_TYPE=Debug` more better
message(STATUS "Build type: ${CMAKE_BUILD_TYPE}")

# Compile options for Debug variant
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -g -O0")

# Compile options for Release variant
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -O2")

message(STATUS "Compile options for c++: ${CMAKE_CXX_FLAGS}")

##--------------------- Global Macros --------------------------------------##
add_definitions(-DDEBUG -DREAL_COOL_ENGINEER)

##--------------------- Include directories --------------------------------##
include_directories(src)

##--------------------- Source files ---------------------------------------##
file(GLOB_RECURSE INCLUDE_LIB_SRC
    src/include/*.cpp
)
add_library(include STATIC ${INCLUDE_LIB_SRC})

add_executable(add_item src/add_item.cpp)
target_link_libraries(add_item include)

