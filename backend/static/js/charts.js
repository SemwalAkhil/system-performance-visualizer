// =====================
// CONFIG (shared)
// =====================
const MAX_POINTS = 10;
// const API_BASE = window.API_BASE || '/api';

// =====================
// STATE
// =====================
let cpuData = Array(MAX_POINTS).fill(0);
let memoryData = Array(MAX_POINTS).fill(0);
let labels = Array(MAX_POINTS).fill("--");

// =====================
// CHART INITIALIZATION
// =====================
function createChart(ctx, label, dataArray, color) {
    return new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label,
                data: dataArray,
                borderColor: color,
                backgroundColor: color + '22',
                borderWidth: 2,
                pointRadius: 2,
                fill: true
            }]
        },
        options: {
            animation: false,
            responsive: true,
            scales: {
                y: { min: 0, max: 100 },
                x: { ticks: { maxRotation: 0 } }
            },
            elements: { line: { tension: 0.3 } }
        }
    });
}


const cpuChart = createChart(document.getElementById("cpuChart"), 'CPU %', cpuData, '#00c8e8');
const memoryChart = createChart(document.getElementById("memoryChart"), 'Memory %', memoryData, '#7c5cfc');

// =====================
// CLOCK
// =====================
function updateClock() {
    const clock = document.getElementById("clock");
    if (clock) clock.innerText = new Date().toLocaleTimeString();
}
setInterval(updateClock, 1000);
updateClock();

// =====================
// STAT CARDS UPDATE
// =====================
function updateStatCards(cpu, memory) {
    const cpuBadge = document.getElementById('cpu-badge');
    if (cpuBadge) cpuBadge.textContent = cpu.toFixed(1) + '%';

    const memBadge = document.getElementById('mem-badge');
    if (memBadge) memBadge.textContent = memory.toFixed(1) + '%';

    const loadEl = document.getElementById('system-load');
    if (loadEl) loadEl.textContent = (cpu / 100).toFixed(2);

    const procRows = document.querySelectorAll('#process-inputs .proc-row');
    const activeProcEl = document.getElementById('active-processes');
    if (activeProcEl) activeProcEl.textContent = procRows.length;
}

// =====================
// STATS (SLIDING WINDOW)
// =====================
async function fetchStats() {
    try {
        const res = await fetch(`${API_BASE}/stats`);
        const data = await res.json();

        if (labels.length >= MAX_POINTS) {
            labels.shift();
            cpuData.shift();
            memoryData.shift();
        }

        labels.push(new Date().toLocaleTimeString());
        cpuData.push(data.cpu);
        memoryData.push(data.memory);

        cpuChart.update();
        memoryChart.update();

        updateStatCards(data.cpu, data.memory);
    } catch (err) {
        console.warn("Stats fetch skipped");
    }
}
setInterval(fetchStats, 1000);
