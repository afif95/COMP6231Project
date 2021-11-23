import time

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home_route():
    return "<p>COMP 6231 Project home page.</p>"


@app.route("/unresponsive-endpoint")
def unresponsive_endpoint():
    time.sleep(5)
    return "<p>This endpoint is slow by design.</p>"


if __name__ == "__main__":
    app.run(debug=True)
