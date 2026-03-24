#include <iostream>
#include <vector>
using namespace std;

struct Process {
    int id, arrival, burst, completion, waiting, turnaround;
};

void fcfs(vector<Process>& p) {
    int time = 0;

    for (auto &proc : p) {
        if (time < proc.arrival)
            time = proc.arrival;

        proc.completion = time + proc.burst;
        proc.turnaround = proc.completion - proc.arrival;
        proc.waiting = proc.turnaround - proc.burst;

        time = proc.completion;
    }
}

int main() {
    vector<Process> p = {
        {1, 0, 5},
        {2, 1, 3},
        {3, 2, 8}
    };

    fcfs(p);

    cout << "ID\tAT\tBT\tCT\tWT\tTAT\n";

    for (auto &proc : p) {
        cout << proc.id << "\t"
             << proc.arrival << "\t"
             << proc.burst << "\t"
             << proc.completion << "\t"
             << proc.waiting << "\t"
             << proc.turnaround << "\n";
    }

    return 0;
}