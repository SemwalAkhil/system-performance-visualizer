// =====================
// CONFIG (shared)
// =====================
// use global API_BASE from HTML
// (avoid redeclaration across multiple JS files)


// =====================
// STATE
// =====================
// const API_BASE = window.API_BASE || '/api';
let ganttBlocks = [];
let executionInterval = null;
let hasStartedExecution = false;

// =====================
// PROCESS INPUT
// =====================
let processCounter = document.querySelectorAll('#process-inputs .proc-row').length || 1;

function addProcess() {
    processCounter++;
    const div = document.createElement("div");
    div.className = "proc-row";

    div.innerHTML = `
        <span class="proc-id-label">P${processCounter}</span>
        <input type="number" class="arrival proc-input" placeholder="0" min="0" />
        <input type="number" class="burst proc-input" placeholder="1" min="1" />
        <button class="proc-remove-btn" onclick="removeProcess(this)" title="Remove">✕</button>
    `;

    document.getElementById("process-inputs").appendChild(div);
}

function removeProcess(btn) {
    btn.parentElement.remove();

    // Re-label remaining rows
    const rows = document.querySelectorAll('#process-inputs .proc-row');
    rows.forEach((row, i) => {
        const label = row.querySelector('.proc-id-label');
        if (label) label.textContent = `P${i + 1}`;
    });

    processCounter = rows.length;
}

// =====================
// VALIDATION
// =====================
function validateProcesses(arrivals, bursts) {
    for (let i = 0; i < arrivals.length; i++) {
        const a = parseInt(arrivals[i].value);
        const b = parseInt(bursts[i].value);
        if (isNaN(a) || isNaN(b)) { alert("Please fill all fields correctly"); return false; }
        if (b <= 0) { alert("Burst time must be greater than 0"); return false; }
        if (a < 0) { alert("Arrival time cannot be negative"); return false; }
    }
    return true;
}

// =====================
// SCHEDULER
// =====================
async function runScheduler() {
    // clear any previous execution loop
    if (executionInterval) clearInterval(executionInterval);
    // reset execution state for a fresh run
    hasStartedExecution = false;

    const arrivals = document.querySelectorAll(".arrival");
    const bursts = document.querySelectorAll(".burst");

    

    if (!validateProcesses(arrivals, bursts)) return;

    const runBtn = document.getElementById("run-btn");
    if (runBtn) {
        runBtn.innerText = "Running..."
        runBtn.disabled = true;
    }
    // capture process count BEFORE execution
    const procRows = document.querySelectorAll('#process-inputs .proc-row');
    totalProcesses = procRows.length;
    simulationStarted = false; // still not started yet
    const processes = Array.from(arrivals).map((_, i) => ({
        id: i + 1,
        arrival: parseInt(arrivals[i].value),
        burst: parseInt(bursts[i].value)
    }));

    try {
        const res = await fetch(`${API_BASE}/scheduler`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(processes)
        });
        const data = await res.json();

        renderTable(data.processes);
        renderGantt(data.processes);
        renderAverages(data.processes);
        startRealtimeExecution(data.processes, runBtn);
    } catch (err) {
        console.error("Scheduler error:", err);
        if (runBtn) {
                runBtn.disabled = false;
                runBtn.innerText = "▶ Start Simulation";
            }
    }
}

// =====================
// TABLE + AVERAGES
// =====================
function renderTable(data) {
    const tbody = document.getElementById('scheduler-body');

    
    

    tbody.innerHTML = data.map(p => `
        <tr id="row-${p.id}">
            <td>${p.id}</td>
            <td>${p.arrival}</td>
            <td>${p.burst}</td>
            <td>${p.start}</td>
            <td>${p.completion}</td>
            <td>${p.waiting}</td>
            <td>${p.turnaround}</td>
        </tr>
    `).join('');
}

function renderAverages(data) {
    const avgWT = data.reduce((s, p) => s + p.waiting, 0) / data.length;
    const avgTAT = data.reduce((s, p) => s + p.turnaround, 0) / data.length;
    const avgDiv = document.getElementById("averages");
    if (avgDiv) {
        avgDiv.innerHTML = `
            <p>Average Waiting Time: ${avgWT.toFixed(2)}</p>
            <p>Average Turnaround Time: ${avgTAT.toFixed(2)}</p>
        `;
    }
}

// =====================
// GANTT (WITH IDLE)
// =====================
function renderGantt(data) {
    const gantt = document.getElementById("gantt");
    const timelineDiv = document.getElementById("timeline");
    gantt.innerHTML = ""; timelineDiv.innerHTML = ""; ganttBlocks = [];

    let prevCompletion = 0;
    const totalTime = data.length ? data[data.length - 1].completion : 1;

    data.forEach((p, index) => {
        if (p.start > prevCompletion) {
            const idleWidth = ((p.start - prevCompletion) / totalTime) * 100;
            const idleBlock = document.createElement("div");
            idleBlock.style.width = idleWidth + "%";
            idleBlock.style.backgroundColor = "#9ca3af";
            idleBlock.innerText = "IDLE";
            gantt.appendChild(idleBlock);

            const idleTime = document.createElement("div");
            idleTime.style.width = idleWidth + "%";
            idleTime.innerText = prevCompletion;
            timelineDiv.appendChild(idleTime);
        }

        const width = (p.burst / totalTime) * 100;
        const block = document.createElement("div");
        block.style.width = width + "%";
        block.style.backgroundColor = getColor(index);
        block.innerText = `P${p.id}`;
        gantt.appendChild(block);
        ganttBlocks.push(block);

        const time = document.createElement("div");
        time.style.width = width + "%";
        time.innerText = p.start;
        timelineDiv.appendChild(time);

        prevCompletion = p.completion;
    });

    if (data.length) {
        const end = document.createElement("div");
        end.innerText = data[data.length - 1].completion;
        timelineDiv.appendChild(end);
    }
}

function getColor(i) {
    const colors = ["#00b4d8", "#7c3aed", "#10b981", "#f59e0b", "#ef4444"];
    return colors[i % colors.length];
}

// =====================
// EXECUTION SYNC
// =====================
function startRealtimeExecution(processes, runBtn) {
    if (executionInterval) clearInterval(executionInterval);

    executionInterval = setInterval(async () => {
        try {
            const res = await fetch(`${API_BASE}/current`);
            const data = await res.json();
            const current = parseInt(data.current);

            // CHECK IF EXECUTION COMPLETED (only after execution actually started)
            if (data.done && hasStartedExecution) {
                const label = document.getElementById("current-process");
                if (label) label.innerText = "Execution Complete";

                // CLEAR ALL HIGHLIGHTS ON FINISH
                ganttBlocks.forEach(b => b.classList.remove("active"));
                document.querySelectorAll("#scheduler-body tr").forEach(r => r.classList.remove("active"));

                if (runBtn) {
                    runBtn.disabled = false;
                    runBtn.innerText = "▶ Start Simulation";
                }

                clearInterval(executionInterval);
                hasStartedExecution = false;
                simulationStarted = false;
                totalProcesses = 0;
                return;
            }
            
            

            ganttBlocks.forEach(b => b.classList.remove("active"));
            document.querySelectorAll("#scheduler-body tr").forEach(r => r.classList.remove("active"));

            const label = document.getElementById("current-process");

            // mark that execution has started when first process runs
            if (!isNaN(current)) {
                hasStartedExecution = true;
                simulationStarted = true; // ADD THIS LINE
            }

            if (isNaN(current)) {
                // CPU is idle (but execution may not be finished)
                if (label) label.innerText = "CPU Idle";
                return; // DO NOT stop execution here
            }

            const index = processes.findIndex(p => p.id === current);
            if (index !== -1 && ganttBlocks[index]) {
                ganttBlocks[index].classList.add("active");
                const row = document.getElementById(`row-${current}`);
                if (row) row.classList.add("active");
                if (label) label.innerText = `Running: P${current}`;
            }
        } catch (err) {
            console.warn("Execution sync skipped");
        }
    }, 500);
}
