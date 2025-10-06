# app.py - System Metrics Dashboard with Token Authentication
from flask import Flask, jsonify, render_template, request, abort
import psutil, os

app = Flask(__name__)

# -------------------------------
# Security: Read token from environment
# -------------------------------
# In OpenShift, we will create a secret:
# oc create secret generic metrics-token --from-literal=TOKEN=YourSecretToken
# and inject it into the deployment as environment variable METRICS_TOKEN
TOKEN = os.environ.get("METRICS_TOKEN")

# -------------------------------
# JSON API Endpoint: /metrics
# -------------------------------
# Returns CPU and Memory usage
# Token authentication ensures only authorized access
@app.route("/metrics")
def metrics():
    auth_header = request.headers.get("Authorization")  # Get token from request header
    if auth_header != f"Bearer {TOKEN}":  # Validate token
        abort(401)  # Unauthorized if token is missing/invalid
    
    # Gather system metrics
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    return jsonify({"cpu": cpu, "memory": mem})

# -------------------------------
# HTML Dashboard: /
# -------------------------------
# Serves a simple frontend dashboard with live metrics
@app.route("/")
def dashboard():
    return render_template("index.html")

# -------------------------------
# Main Application
# -------------------------------
if __name__ == "__main__":
    # Use PORT environment variable provided by OpenShift, default 8080
    port = int(os.environ.get("PORT", 8080))
    # Host 0.0.0.0 allows access from outside container
    app.run(host="0.0.0.0", port=port)





# add a comment line at the end
# CI/CD test

