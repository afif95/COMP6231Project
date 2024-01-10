import os

print("kubectl delete deployments comp6231-project-depl -n 10001")
os.system("kubectl delete deployments comp6231-project-depl -n 10001")

print("_________________________________________________________")
print("kubectl delete hpa comp6231-project-depl -n 10001")
os.system("kubectl delete hpa comp6231-project-depl -n 10001")

print("_________________________________________________________")
print("kubectl delete namespace 10001")
os.system("kubectl delete namespace 10001")

print("_________________________________________________________")
print("minikube stop -p multinode-demo")
os.system("minikube stop -p multinode-demo")
