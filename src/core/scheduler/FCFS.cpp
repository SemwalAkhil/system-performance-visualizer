#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream> 
using namespace std;

/*
    Structure to represent a process in scheduling
*/
struct Process {
    int id;         // Process ID
    int arrival;    // Arrival Time (AT)
    int burst;      // Burst Time (BT)

    int completion; // Completion Time (CT)
    int waiting;    // Waiting Time (WT)
    int turnaround; // Turnaround Time (TAT)
};

/*
    FCFS Scheduling Function

    - Processes are executed in order of arrival time
    - Non-preemptive: once a process starts, it runs till completion
*/
void fcfs(vector<Process>& processes) {

    // Sort processes based on arrival time
    sort(processes.begin(), processes.end(),
         [](Process a, Process b) {
             return a.arrival < b.arrival;
         });

    int currentTime = 0; // Tracks current CPU time

    for (auto &p : processes) {

        /*
            If CPU is idle (no process has arrived yet),
            jump time to the arrival of current process
        */
        if (currentTime < p.arrival) {
            currentTime = p.arrival;
        }

        /*
            Completion Time (CT)
            = current time + burst time
        */
        p.completion = currentTime + p.burst;

        /*
            Turnaround Time (TAT)
            = Completion Time - Arrival Time
        */
        p.turnaround = p.completion - p.arrival;

        /*
            Waiting Time (WT)
            = Turnaround Time - Burst Time
        */
        p.waiting = p.turnaround - p.burst;

        // Move current time forward
        currentTime = p.completion;
    }
}

/*
    Convert scheduling result to JSON format
*/
string toJSON(const vector<Process>& processes) {

    stringstream ss;
    ss << "[";

    for (size_t i = 0; i < processes.size(); i++) {
        const auto &p = processes[i];

        ss << "{";
        ss << "\"id\":" << p.id << ",";
        ss << "\"arrival\":" << p.arrival << ",";
        ss << "\"burst\":" << p.burst << ",";
        ss << "\"completion\":" << p.completion << ",";
        ss << "\"waiting\":" << p.waiting << ",";
        ss << "\"turnaround\":" << p.turnaround;
        ss << "}";

        if (i != processes.size() - 1)
            ss << ",";
    }

    ss << "]";
    return ss.str();
}

/*
    Main function to test FCFS scheduling
*/
int main() {

    vector<Process> processes = {
        {1, 0, 5},
        {2, 1, 3},
        {3, 2, 8},
        {4, 3, 6}
    };

    fcfs(processes);

    // Output JSON instead of table
    cout << toJSON(processes);

    return 0;
}