cmake_minimum_required(VERSION 3.12)
project(labneura)

set(CMAKE_CXX_STANDARD 17)

# Check if we're on macOS and using Apple M1 for LLVM Clang++ and OpenMP
if (CMAKE_SYSTEM_NAME MATCHES "Darwin")
    if (CMAKE_SYSTEM_PROCESSOR MATCHES "arm64")
        # Check if LLVM Clang++ exists
        if (EXISTS "/opt/homebrew/opt/llvm/bin/clang++")
            set(CMAKE_CXX_COMPILER "/opt/homebrew/opt/llvm/bin/clang++")
        else()
            message(FATAL_ERROR "LLVM Clang++ not found. Please install it via Homebrew.")
        endif()
        if (EXISTS "/opt/homebrew/opt/libomp")
            set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Xpreprocessor -fopenmp -lomp -I/opt/homebrew/opt/libomp/include -L/opt/homebrew/opt/libomp/lib ${CMAKE_CXX_FLAGS} ${TORCH_CXX_FLAGS}")
            set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Xpreprocessor -fopenmp -lomp -I/opt/homebrew/opt/libomp/include -L/opt/homebrew/opt/libomp/lib")
        else()
            message(FATAL_ERROR "OpenMP not found. Please install OpenMP on your system.")
        endif()
    else()
        message(FATAL_ERROR "Unsupported architecture on macOS. Only Apple M1 is supported.")
    endif()
endif()

# To get the Python Site-Packages PATH
execute_process(
    COMMAND python -c "import site; print(site.getsitepackages()[0])"
    OUTPUT_VARIABLE PYTHON_SITE_PACKAGES
    OUTPUT_STRIP_TRAILING_WHITESPACE
)

if(APPLE)
    set(CMAKE_SHARED_LINKER_FLAGS "-undefined dynamic_lookup")
endif()

# Include PYBIND11 and OpenMP directories
find_package(pybind11 REQUIRED)
include_directories(${PYBIND11_INCLUDE_DIR})
# find_package(openMP REQUIRED)

# Include Torch directories
set(Torch_DIR /Users/gtk/GTK/LabNeura/env/lib/python3.11/site-packages/torch/share/cmake/Torch)
find_package(Torch REQUIRED)
include_directories(${TORCH_INCLUDE_DIRS})

# Include Labneura includes 
include_directories(include)

# Add library for Algorithms
add_library(labneura MODULE bindings/interface.cpp 
    src/algorithms/sorting.cpp 
    src/algorithms/graph.cpp
    src/data/tensor.cpp
    )
target_include_directories(labneura PRIVATE ${TORCH_INCLUDE_DIRS})
# target_link_libraries(labneura PRIVATE pybind11::module OpenMP::OpenMP_CXX "${TORCH_LIBRARIES}")
target_link_libraries(labneura PRIVATE pybind11::module "${TORCH_LIBRARIES}")
set_target_properties(labneura PROPERTIES PREFIX "${PYTHON_MODULE_PREFIX}" SUFFIX "${PYTHON_MODULE_EXTENSION}")
set_property(TARGET labneura PROPERTY CXX_STANDARD 17)

if (CMAKE_SYSTEM_PROCESSOR MATCHES "arm64")
    target_compile_options(labneura PRIVATE -mcpu=apple-m1)
else()
    if (CMAKE_CXX_COMPILER_ID MATCHES "Clang")
        target_compile_options(labneura PRIVATE -march=native)
    endif()
endif()