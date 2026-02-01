#include "LinuxSystemMonitor.h"
#include <fstream>
#include <sstream>
#include <string>

// Constructor that initializes prevTotal and prevIdle to 0.
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

// Returns the current percentage of CPU utilization on a Linux system.
double LinuxSystemMonitor::getCPUUsage()
{
    std::ifstream statFile("/proc/stat");
    std::string line;

    // Read the first line of /proc/stat, which contains statistics for all CPUs.
    std::getline(statFile, line);

    // Use an istringstream to parse the values from the line.
    std::istringstream ss(line);
    std::string cpuLabel;

    long long user, nice, system, idle, iowait, irq, softirq, steal;

    // Read the CPU usage statistics into variables.
    ss >> cpuLabel >> user >> nice >> system >> idle >> iowait >> irq >> softirq >> steal;

    // Calculate the total time and idle time for the current CPU.
    long long idleTime = idle + iowait;
    long long totalTime =
        user + nice + system + idle + iowait + irq + softirq + steal;

    // If this is the first call, initialize prevTotal and prevIdle to the current total and idle times.
    if (prevTotal == 0)
    {
        prevTotal = totalTime;
        prevIdle = idleTime;
        return 0.0;
    }

    // Calculate the change in CPU time since the last update.
    long long totalDelta = totalTime - prevTotal;
    long long idleDelta = idleTime - prevIdle;

    // Update prevTotal and prevIdle with the current total and idle times.
    prevTotal = totalTime;
    prevIdle = idleTime;

    // If no change in CPU time occurred, return 0.0 to avoid division by zero.
    if (totalDelta == 0)
        return 0.0;

    // Calculate the percentage of CPU usage based on the change in time and idle time.
    return (1.0 - (double)idleDelta / totalDelta) * 100.0;
}
