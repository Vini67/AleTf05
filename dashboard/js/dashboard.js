async function loadData() {
    const statusRes = await fetch("http://localhost:5000/health/status");
    const status = await statusRes.json();

    const metricsRes = await fetch("http://localhost:5000/metrics");
    const metrics = await metricsRes.json();

    document.getElementById("db-status").innerText = status.database ? "OK" : "FAIL";
    document.getElementById("backend-response").innerText = metrics.response_time + "ms";
}

setInterval(loadData, 3000);