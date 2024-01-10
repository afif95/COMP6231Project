import time
import socket
from flask import Flask, render_template
import json
import os
import subprocess
import json, sys, yaml

from kubernetes import client, config

config.load_kube_config()
v1 = client.AutoscalingV1Api()
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home_route():
    return render_template("autoscaling-demo.html")


@app.route("/unresponsive-endpoint", methods=["GET", "POST"])
def unresponsive_endpoint():
    time.sleep(5)
    return "<p>This endpoint is slow by design.</p>"


@app.route("/autoscaling-demo", methods=["GET"])
def autoscaling_demo():
    hpa = v1.list_namespaced_horizontal_pod_autoscaler('default')

    vpa = subprocess.check_output("kubectl get -o yaml vpa -n default", shell=True)
    vpa = yaml.safe_load(vpa)
    autoscaling_data = {
        "hpa_events": {
            "configuration": {
                "name": hpa.items[0].metadata.name,
                "namespace": hpa.items[0].metadata.namespace,
                "min_replicas": hpa.items[0].spec.min_replicas,
                "max_replicas": hpa.items[0].spec.max_replicas,
                "target_cpu_utilization_percentage": hpa.items[0].spec.target_cpu_utilization_percentage
            },
            "status": {
                "current_replicas": hpa.items[0].status.current_replicas,
                "desired_replicas": hpa.items[0].status.desired_replicas,
                "current_cpu_utilization_percentage": hpa.items[0].status.current_cpu_utilization_percentage
            }
         },
        "vpa_events": {
            "lowerBound": {
                "cpu": vpa["items"][0]["status"]["recommendation"]["containerRecommendations"][0]["lowerBound"]["cpu"],
                "memory": vpa["items"][0]["status"]["recommendation"]["containerRecommendations"][0]["lowerBound"]["memory"]
            },
            "target": {
                "cpu": vpa["items"][0]["status"]["recommendation"]["containerRecommendations"][0]["target"]["cpu"],
                "memory": vpa["items"][0]["status"]["recommendation"]["containerRecommendations"][0]["target"]["memory"]
            },
            "upperBound": {
                "cpu": vpa["items"][0]["status"]["recommendation"]["containerRecommendations"][0]["upperBound"]["cpu"],
                "memory": vpa["items"][0]["status"]["recommendation"]["containerRecommendations"][0]["upperBound"]["memory"]
            }
        }
    }

    return json.dumps(autoscaling_data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9000)

