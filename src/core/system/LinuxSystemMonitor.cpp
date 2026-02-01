#include "LinuxSystemMonitor.h"
#include <fstream>
#include <sstream>
#include <string>

LinuxSystemMonitor::LinuxSystemMonitor()
    : prevTotal(0), prevIdle(0) {}

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

double LinuxSystemMonitor::getCPUUsage()
{
    std::ifstream statFile("/proc/stat");
    std::string line;
    std::getline(statFile, line);

    std::istringstream ss(line);
    std::string cpuLabel;

    long long user, nice, system, idle, iowait, irq, softirq, steal;

    ss >> cpuLabel >> user >> nice >> system >> idle >> iowait >> irq >> softirq >> steal;

    long long idleTime = idle + iowait;
    long long totalTime =
        user + nice + system + idle + iowait + irq + softirq + steal;

    if (prevTotal == 0)
    {
        prevTotal = totalTime;
        prevIdle = idleTime;
        return 0.0;
    }

    long long totalDelta = totalTime - prevTotal;
    long long idleDelta = idleTime - prevIdle;

    prevTotal = totalTime;
    prevIdle = idleTime;

    if (totalDelta == 0)
        return 0.0;

    return (1.0 - (double)idleDelta / totalDelta) * 100.0;
}
