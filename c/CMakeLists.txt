cmake_minimum_required(VERSION 3.26.3 FATAL_ERROR)
project(project_nn_c LANGUAGES C)


option(core_compile "" ON)
option(print_compile "" ON)
option(svm_compile "" ON)


set(CMAKE_GENERATOR MinGW Makefiles)
set(CMAKE_BINARY_DIR ${CMAKE_SOURCE_DIR}/build)
set(CMAKE_BUILD_TYPE Debug)
set(COMPILE_OPTIONS
	-Wall
	-Wextra
	-Wpedantic
)
set(COMPILE_FEATURES 
	c_std_23
)


if (core_compile)
	message("CORE COMPILATION")
	add_subdirectory(core)
endif()

if (print_compile)
	message("PRINT COMPILATION")
	add_subdirectory(print)
endif()

if (svm_compile)
	message("SVM COMPILATION")
	add_subdirectory(svm)
endif()
