from flask import Flask, jsonify, render_template
import psutil, os

app = Flask(__name__)

# JSON endpoint for metrics
@app.route("/metrics")
def metrics():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    return jsonify({"cpu": cpu, "memory": mem})

# HTML dashboard
@app.route("/")
def dashboard():
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

