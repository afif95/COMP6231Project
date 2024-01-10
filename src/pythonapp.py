import time
import socket
from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home_route():
    return render_template("index.html")


@app.route("/unresponsive-endpoint", methods=["GET", "POST"])
def unresponsive_endpoint():
    time.sleep(5)
    return "<p>This endpoint is slow by design.</p>"


@app.route("/load-balancing-demo", methods=["GET"])
def load_balancing_demo():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    host_data = {
        "hostname": hostname,
        "ip_address": ip_address
    }
    return json.dumps(host_data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5005)

