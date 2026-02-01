#include <iostream>
#include "core/system/LinuxSystemMonitor.h"
#include <thread>
#include <chrono>

int main()
{
    LinuxSystemMonitor monitor;
    while (true)
    {
        std::cout << "Memory Usage: "
                  << monitor.getMemoryUsage()
                  << "%\n";

        std::cout << "CPU Usage: "
                  << monitor.getCPUUsage()
                  << "%\n";

        std::this_thread::sleep_for(std::chrono::seconds(1));
    }

    return 0;
}
