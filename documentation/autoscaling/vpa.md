### Links ###
* https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler
* https://cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler
#### More links to be added... ####

To use VPA, you need to install it first as it is not automatically provided by the Kubernetes like HPA. Below are the steps:
1. Ensure you are using latest openssl version available for your system
2. git clone
3. cd autoscaler/vertical-pod-autoscaler
4. ./hack/vpa-down.sh
5. ./hack/vpa-up.sh 
Note: If you are seeing following error during this step:
unknown option -addext
please upgrade openssl 
6. ./hack/vpa-process-yamls.sh print
7. kubectl describe vpa -> to check if the vpa has been created