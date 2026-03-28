// =====================
// CONFIG (shared)
// =====================
const MAX_POINTS = 10;

// =====================
// STATE
// =====================
let cpuData = Array(MAX_POINTS).fill(0);
let memoryData = Array(MAX_POINTS).fill(0);
let labels = Array(MAX_POINTS).fill("--");

// =====================
// CHART INITIALIZATION
// =====================
function createChart(ctx, label, dataArray) {
    return new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{ label, data: dataArray }]
        },
        options: {
            animation: false,
            responsive: true,
            scales: { y: { min: 0, max: 100 } },
            elements: { line: { tension: 0.3 } }
        }
    });
}

const cpuChart = createChart(document.getElementById("cpuChart"), 'CPU %', cpuData);
const memoryChart = createChart(document.getElementById("memoryChart"), 'Memory %', memoryData);

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
    } catch (err) {
        console.warn("Stats fetch skipped");
    }
}
setInterval(fetchStats, 1000);
