#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <regex>
using namespace std;

/*
    Structure to represent a process in scheduling
*/
struct Process
{
    int id;      // Process ID
    int arrival; // Arrival Time (AT)
    int burst;   // Burst Time (BT)

    int start;      // Start Time (ST)
    int completion; // Completion Time (CT)
    int waiting;    // Waiting Time (WT)
    int turnaround; // Turnaround Time (TAT)
};

/*
    FCFS Scheduling Function
*/
void fcfs(vector<Process> &processes)
{
    sort(processes.begin(), processes.end(),
         [](Process a, Process b)
         {
             return a.arrival < b.arrival;
         });

    int currentTime = 0;

    for (auto &p : processes)
    {
        if (currentTime < p.arrival)
        {
            currentTime = p.arrival;
        }

        p.start = currentTime;
        p.completion = currentTime + p.burst;
        p.turnaround = p.completion - p.arrival;
        p.waiting = p.turnaround - p.burst;

        currentTime = p.completion;
    }
}

/*
    Convert scheduling result + timeline to JSON
*/
string toJSON(const vector<Process> &processes)
{
    stringstream ss;

    // Generate timeline
    vector<int> timeline;
    for (const auto &p : processes)
    {
        for (int t = p.start; t < p.completion; t++)
        {
            timeline.push_back(p.id);
        }
    }

    ss << "{";

    // 🔹 Processes array
    ss << "\"processes\":[";
    for (size_t i = 0; i < processes.size(); i++)
    {
        const auto &p = processes[i];

        ss << "{";
        ss << "\"id\":" << p.id << ",";
        ss << "\"arrival\":" << p.arrival << ",";
        ss << "\"burst\":" << p.burst << ",";
        ss << "\"start\":" << p.start << ",";
        ss << "\"completion\":" << p.completion << ",";
        ss << "\"waiting\":" << p.waiting << ",";
        ss << "\"turnaround\":" << p.turnaround;
        ss << "}";

        if (i != processes.size() - 1)
            ss << ",";
    }
    ss << "],";

    // 🔹 Timeline array
    ss << "\"timeline\":[";
    for (size_t i = 0; i < timeline.size(); i++)
    {
        ss << timeline[i];
        if (i != timeline.size() - 1)
            ss << ",";
    }
    ss << "]";

    ss << "}";

    return ss.str();
}

/*
    Main function
*/
int main()
{
    string input;
    getline(cin, input);

    vector<Process> processes;

    // Flexible regex (handles spaces)
    regex pattern(R"(\{\s*"id"\s*:\s*(\d+)\s*,\s*"arrival"\s*:\s*(\d+)\s*,\s*"burst"\s*:\s*(\d+)\s*\})");
    smatch match;

    string::const_iterator searchStart(input.cbegin());

    while (regex_search(searchStart, input.cend(), match, pattern))
    {
        Process p;

        p.id = stoi(match[1]);
        p.arrival = stoi(match[2]);
        p.burst = stoi(match[3]);

        processes.push_back(p);

        searchStart = match.suffix().first;
    }

    fcfs(processes);

    cout << toJSON(processes);

    return 0;
}