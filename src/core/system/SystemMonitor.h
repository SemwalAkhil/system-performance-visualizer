#ifndef SYSTEM_MONITOR_H
#define SYSTEM_MONITOR_H

// SystemMonitor class provides an interface for monitoring the system's CPU and memory usage.
class SystemMonitor
{
public:
    // Virtual destructor to ensure proper cleanup of derived classes.
    virtual ~SystemMonitor() {}

    // Pure virtual function that returns the current percentage of CPU utilization.
    // Must be implemented by derived classes.
    virtual double getCPUUsage() = 0;

    // Pure virtual function that returns the current percentage of memory usage.
    // Must be implemented by derived classes.
    virtual double getMemoryUsage() = 0;
};

#endif
