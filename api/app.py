from flask import Flask, jsonify
import time
from models.metrics import save_metric
from healthchecks.tcp_check import check_tcp
from healthchecks.db_check import check_db

app = Flask(__name__)

# Função de alertas (simples, imprime no console)
def send_alert(service, message):
    print(f"🚨 ALERTA [{service}]: {message}")

# Endpoint básico de saúde
@app.route("/health")
def health():
    return jsonify({
        "status": "OK",
        "timestamp": time.time()
    })

# Endpoint de status dos serviços
@app.route("/health/status")
def health_status():
    start = time.time()

    tcp = check_tcp("db", 3306)
    db = check_db()

    response_time = (time.time() - start) * 1000

    # ALERTAS
    if not tcp:
        send_alert("TCP", "Porta do banco não está acessível")
    if not db:
        send_alert("DATABASE", "Falha na conexão com banco")

    # SALVAR NO BANCO
    save_metric("tcp", "ok" if tcp else "fail", response_time)
    save_metric("database", "ok" if db else "fail", response_time)

    return jsonify({
        "tcp": tcp,
        "database": db
    })

# Endpoint agregando status de todos os serviços
@app.route("/health/all")
def health_all():
    tcp_status = "ok" if check_tcp("db", 3306) else "fail"
    db_status = "ok" if check_db() else "fail"

    return jsonify({
        "backend": "ok",
        "database": db_status,
        "tcp": tcp_status,
        "redis": "ok"  # placeholder, pode implementar depois
    })

# Endpoint de métricas
@app.route("/metrics")
def metrics():
    return jsonify({
        "response_time": 120,  # placeholder, você pode medir real
        "uptime": "99.9%",
        "timestamp": time.time()
    })

# Endpoint de relatório completo
@app.route("/health/report")
def health_report():
    tcp = check_tcp("db", 3306)
    db = check_db()

    report = {
        "services": {
            "backend": {"healthy": True},
            "database": {"healthy": db},
            "tcp": {"healthy": tcp}
        },
        "generated_at": time.time()
    }
    return jsonify(report)

if __name__ == "__main__":
    # Importante: host 0.0.0.0 para expor fora do container
    app.run(host="0.0.0.0", port=5000)