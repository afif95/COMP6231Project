import os

print("kubectl create -f ../deploymentconfig/vpa-configuration.yaml -n 10001")
os.system("kubectl create -f ../deploymentconfig/vpa-configuration.yaml -n 10001")

print("_________________________________________________________")
print("kubectl autoscale deployment comp6231-project-depl --cpu-percent=3 --min=1 --max=10 -n 10001")
os.system("kubectl autoscale deployment comp6231-project-depl --cpu-percent=3 --min=1 --max=10 -n 10001")

print("_________________________________________________________")
print("minikube service comp6231-project-service -p multinode-demo -n 10001")
os.system("minikube service comp6231-project-service -p multinode-demo -n 10001")

"""print("_________________________________________________________")
print("kubectl describe pdb comp6231-project-depl-pdb -n 10001")
os.system("kubectl describe pdb comp6231-project-depl-pdb -n 10001")"""
