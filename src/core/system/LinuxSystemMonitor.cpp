#include "LinuxSystemMonitor.h"
#include <fstream>
#include <sstream>
#include <string>
#include <thread>
#include <chrono>

// Constructor that initializes prevTotal and prevIdle to 0.
LinuxSystemMonitor::LinuxSystemMonitor()
    : prevTotal(0), prevIdle(0) {}

// Returns the current percentage of memory usage on a Linux system.
double LinuxSystemMonitor::getMemoryUsage()
{
    std::ifstream meminfo("/proc/meminfo");

    std::string key;
    long value;
    std::string unit;

    long memTotal = 0;
    long memAvailable = 0;

    while (meminfo >> key >> value >> unit)
    {
        if (key == "MemTotal:")
            memTotal = value;
        else if (key == "MemAvailable:")
        {
            memAvailable = value;
            break;
        }
    }

    if (memTotal == 0)
        return 0.0;

    return 100.0 * (memTotal - memAvailable) / memTotal;
}

// 🔥 FIXED CPU USAGE (DOUBLE READ METHOD)
double LinuxSystemMonitor::getCPUUsage()
{
    auto readCPU = []()
    {
        std::ifstream statFile("/proc/stat");
        std::string line;
        std::getline(statFile, line);

        std::istringstream ss(line);
        std::string cpuLabel;

        long long user, nice, system, idle, iowait, irq, softirq, steal;
        ss >> cpuLabel >> user >> nice >> system >> idle >> iowait >> irq >> softirq >> steal;

        long long idleTime = idle + iowait;
        long long totalTime = user + nice + system + idle + iowait + irq + softirq + steal;

        return std::make_pair(totalTime, idleTime);
    };

    // First read
    auto [total1, idle1] = readCPU();

    // Small delay (IMPORTANT)
    std::this_thread::sleep_for(std::chrono::milliseconds(100));

    // Second read
    auto [total2, idle2] = readCPU();

    long long totalDelta = total2 - total1;
    long long idleDelta = idle2 - idle1;

    if (totalDelta == 0)
        return 0.0;

    return (1.0 - (double)idleDelta / totalDelta) * 100.0;
}