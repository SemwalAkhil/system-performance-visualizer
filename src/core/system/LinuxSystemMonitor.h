#ifndef LINUX_SYSTEM_MONITOR_H
#define LINUX_SYSTEM_MONITOR_H

// LinuxSystemMonitor class provides an implementation of the SystemMonitor interface for Linux systems.
#include "SystemMonitor.h"

class LinuxSystemMonitor : public SystemMonitor
{
public:
    // Constructor that initializes prevTotal and prevIdle to 0.
    LinuxSystemMonitor();

    // Returns the current percentage of CPU utilization on a Linux system.
    double getCPUUsage() override;

    // Returns the current percentage of memory usage on a Linux system.
    double getMemoryUsage() override;

private:
    // Store previous total and idle CPU times to calculate CPU usage changes over time.
    long long prevTotal;
    long long prevIdle;
};

#endif
