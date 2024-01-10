### Prerequisites ###
Prior to executing the scripts, below command is be executed in case you have not created nodes setup in minikube:
  - "minikube start --nodes 2 --extra-config=controller-manager.horizontal-pod-autoscaler-sync-period=5s --extra-config=controller-manager.horizontal-pod-autoscaler-downscale-stabilization=10s -p multinode-demo"
  
###Command to run the scripts ###

* python ((scriptname.py))

### Utilites consists of 3 python scripts: ###

<b> setup_script.py </b>

* This script is required to execute basic commands required for the demonstration. It will perform below activities:
  * Starts multinode-demo
  * Creates namespace 10001
  * Deploys the API
  * Creates Load balancer
  * Enables metrics server if not enabled. It is required for HPA
  * Enables minikube dashboard for multinode-demo
  
<b> execution_script.py </b>

* This script:
  * Exposes the service created by setup_script.py
  * Creates HPA

<b> cleanup_script.py </b>

* The script is required in case if everything has to be cleaned up just so one could start over
  * Deletes deployment
  * Deletes HPA
  * Deletes Load Balancer Service
  * Stops multinode-demo


  
 
