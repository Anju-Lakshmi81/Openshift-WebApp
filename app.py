from flask import Flask, jsonify
import psutil, os

app = Flask(__name__)

@app.route("/metrics")
def metrics():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    return jsonify({"cpu": cpu, "memory": mem})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
