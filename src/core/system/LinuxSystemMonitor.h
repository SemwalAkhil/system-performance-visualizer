#ifndef LINUX_SYSTEM_MONITOR_H
#define LINUX_SYSTEM_MONITOR_H

// LinuxSystemMonitor class provides an implementation of the SystemMonitor interface for Linux systems.
#include "SystemMonitor.h"

class LinuxSystemMonitor : public SystemMonitor
{
public:
    // Returns the current percentage of CPU utilization on a Linux system.
    double getCPUUsage() override;

    // Returns the current percentage of memory usage on a Linux system.
    double getMemoryUsage() override;
};

#endif
