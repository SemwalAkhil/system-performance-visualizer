#include <iostream>
#include <iomanip>
#include "core/system/LinuxSystemMonitor.h"

int main()
{
    LinuxSystemMonitor monitor;

    double cpu = monitor.getCPUUsage();
    double memory = monitor.getMemoryUsage();

    std::cout << std::fixed << std::setprecision(2);
    std::cout << "{";
    std::cout << "\"cpu\": " << cpu << ", ";
    std::cout << "\"memory\": " << memory;
    std::cout << "}";

    return 0;
}
