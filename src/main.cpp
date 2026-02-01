#include <iostream>
#include "core/system/LinuxSystemMonitor.h"

int main()
{
    LinuxSystemMonitor monitor;

    std::cout << "Memory Usage: "
              << monitor.getMemoryUsage()
              << "%\n";

    std::cout << "CPU Usage: "
              << monitor.getCPUUsage()
              << "%\n";

    return 0;
}
