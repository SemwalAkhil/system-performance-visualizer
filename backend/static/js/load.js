// =====================
// CONFIG (shared)
// =====================

// =====================
// LOAD CONTROL (API WRAPPER)
// =====================
async function callAPI(endpoint) {
    try {
        await fetch(`${API_BASE}${endpoint}`, { method: 'POST' });
    } catch (err) {
        console.error(`Error calling ${endpoint}:`, err);
    }
}

// =====================
// CPU CONTROLS
// =====================
function cpuAdd() { return callAPI('/load/cpu/add'); }
function cpuReduce() { return callAPI('/load/cpu/reduce'); }
function cpuStop() { return callAPI('/load/cpu/stop'); }

// =====================
// MEMORY CONTROLS
// =====================
function memoryAdd() { return callAPI('/load/memory/add'); }
function memoryReduce() { return callAPI('/load/memory/reduce'); }
function memoryStop() { return callAPI('/load/memory/stop'); }
