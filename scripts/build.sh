#!/bin/bash

echo "Building C++ system monitor..."

mkdir -p bin

g++ src/main.cpp src/core/system/LinuxSystemMonitor.cpp -o bin/system_monitor

echo "Build complete."