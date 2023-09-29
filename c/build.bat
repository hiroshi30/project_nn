@echo off

rmdir /q /s build
mkdir build

cmake -S . -B build -G "MinGW Makefiles"
cmake --build build --config Debug

build\svm.exe