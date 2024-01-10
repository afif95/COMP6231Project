from flask import Flask
import socket

app = Flask(__name__)
request_counter = 0


@app.route("/counterapp", methods=["GET", "POST"])
def home_route():
    global request_counter
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    request_counter += 1
    return "<p>Counter-app-v2 Serving request number: " + str(request_counter) + " from " + hostname + ":" + ip_address + "</p>"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5005)

