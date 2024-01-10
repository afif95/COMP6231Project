import os
import time

print("_________________________________________________________")
print("minikube start -p multinode-demo")
os.system("minikube start -p multinode-demo")

print("_________________________________________________________")
print("kubectl get nodes")
os.system("kubectl get nodes")

# Check if this can be removed from the script
print("_________________________________________________________")
print("kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.1.0/deploy/static/provider/cloud/deploy.yaml")
os.system("kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.1.0/deploy/static/provider/cloud/deploy.yaml")

print("_________________________________________________________")
print("minikube addons -p multinode-demo enable ingress")
os.system("minikube addons -p multinode-demo enable ingress")

print("_________________________________________________________")
print("minikube tunnel -p multinode-demo")
os.system("minikube tunnel -p multinode-demo")
# Above command requires a terminal

"""print("_________________________________________________________")
print("kubectl create namespace k8s-demo")
os.system("kubectl create namespace k8s-demo")"""

print("_________________________________________________________")
print("kubectl apply -f ../deploymentconfig/comp6231-project-deployment-config.yaml")
os.system("kubectl apply -f ../deploymentconfig/comp6231-project-deployment-config.yaml")

"""print("kubectl apply -f ~/kubernetes_project/abkCOMP6231Project-1/deploymentconfig/comp6231-project-deployment-config.yaml")
os.system("kubectl apply -f ~/kubernetes_project/abkCOMP6231Project-1/deploymentconfig/comp6231-project-deployment-config.yaml")
"""

print("_________________________________________________________")
print("kubectl get pods -o wide")
os.system("kubectl get pods -o wide -n k8s-demo")

print("_________________________________________________________")
print("kubectl apply -f ../deploymentconfig/lb-service.yaml")
os.system("kubectl apply -f ../deploymentconfig/lb-service.yaml")

print("_________________________________________________________")
print("minikube service lb-service --url -p multinode-demo")
os.system("minikube service lb-service --url -p multinode-demo")
# Above command requires a terminal

print("_________________________________________________________")
print("kubectl apply -f ../deploymentconfig/counterapp-depl.yaml")
os.system("kubectl apply -f ../deploymentconfig/counterapp-depl.yaml")

print("_________________________________________________________")
print("kubectl apply -f ../deploymentconfig/counterapp-service.yaml")
os.system("kubectl apply -f ../deploymentconfig/counterapp-service.yaml")

print("_________________________________________________________")
print("minikube service counterapp-service --url -p multinode-demo")
os.system("minikube service counterapp-service --url -p multinode-demo")
# Above command requires a terminal

print("_________________________________________________________")
print("kubectl apply -f ../deploymentconfig/ingress-service.yaml")
os.system("kubectl apply -f ../deploymentconfig/ingress-service.yaml")

print("_________________________________________________________")
print("minikube -p multinode-demo addons enable metrics-server")
os.system("minikube -p multinode-demo addons enable metrics-server")

print("_________________________________________________________")
print("minikube -p multinode-demo addons list | grep metrics-server")
os.system("minikube -p multinode-demo addons list | grep metrics-server")

time.sleep(7)
print("_________________________________________________________")
print("kubectl create -f ../deploymentconfig/vpa-configuration.yaml")
os.system("kubectl create -f ../deploymentconfig/vpa-configuration.yaml")

print("_________________________________________________________")
print("kubectl autoscale deployment comp6231-project --cpu-percent=3 --min=1 --max=10")
os.system("kubectl autoscale deployment comp6231-project --cpu-percent=3 --min=1 --max=10")

"""print("_________________________________________________________")
print("kubectl apply -f ~/kubernetes_project/abkCOMP6231Project-1/deploymentconfig/postdisruptionbudget.yaml -n 10001")
os.system("kubectl apply -f ~/kubernetes_project/abkCOMP6231Project-1/deploymentconfig/postdisruptionbudget.yaml -n 10001")
"""

print("_________________________________________________________")
print("kubectl apply -f ../deploymentconfig/postdisruptionbudget.yaml")
os.system("kubectl apply -f ../deploymentconfig/postdisruptionbudget.yaml")

print("_________________________________________________________")
print("kubectl describe pdb comp6231-project-pdb")
os.system("kubectl describe pdb comp6231-project-pdb")


print("_________________________________________________________")
print("kubectl port-forward --namespace=ingress-nginx service/ingress-nginx-controller 8080:80 5005:80")
os.system("kubectl port-forward --namespace=ingress-nginx service/ingress-nginx-controller 8080:80 5005:80")

"""print("_________________________________________________________")
print("minikube -p multinode-demo dashboard --url")
os.system("minikube -p multinode-demo dashboard --url")"""


