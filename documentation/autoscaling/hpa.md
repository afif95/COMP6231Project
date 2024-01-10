### Links ###
* https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/
* https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/

### Commands ###
* Create HPA: kubectl autoscale deployment comp6231-project --cpu-percent=3 --min=1 --max=10
* Check HPA Details: kubectl describe hpa