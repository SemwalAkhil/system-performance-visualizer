#!/bin/bash

echo "Building C++ system monitor..."

mkdir -p bin

echo "Building system monitor..."
g++ src/main.cpp src/core/system/LinuxSystemMonitor.cpp -o bin/system_monitor

echo "Building FCFS scheduler..."
g++ src/core/scheduler/FCFS.cpp -o bin/fcfs

echo "Build complete."