#include "LinuxSystemMonitor.h"
#include <fstream>
#include <string>

// Returns the current percentage of memory usage on a Linux system.
double LinuxSystemMonitor::getMemoryUsage()
{
    // Open /proc/meminfo for reading memory information.
    std::ifstream meminfo("/proc/meminfo");

    // Declare variables to store the total and available memory values, as well as their units.
    std::string key;
    long value;
    std::string unit;

    // Initialize total and available memory variables to 0.
    long memTotal = 0;
    long memAvailable = 0;

    // Read lines from /proc/meminfo until a matching MemTotal or MemAvailable line is found.
    while (meminfo >> key >> value >> unit)
    {
        if (key == "MemTotal:")
            memTotal = value; // Store the total memory value.
        else if (key == "MemAvailable:")
        {
            memAvailable = value; // Store the available memory value and break out of the loop.
            break;
        }
    }

    // If no MemTotal line was found, return 0 as a default value.
    if (memTotal == 0)
        return 0.0;

    // Calculate the percentage of memory usage by subtracting available memory from total memory,
    // and dividing by the total memory, then multiplying by 100.
    return 100.0 * (memTotal - memAvailable) / memTotal;
}

// TODO: Implement CPU usage calculation using /proc/stat
double LinuxSystemMonitor::getCPUUsage()
{
    // This function will need to parse the output of /proc/stat to determine the total and idle CPU time.
    // It will then calculate the percentage of time the CPU is busy.
    return 0.0;
}
