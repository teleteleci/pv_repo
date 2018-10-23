# Kubernetes

## Comands

#### Minikube
```bash
minikube start --vm-driver=virtualbox
minikube status
kubectl get all --all-namespaces
# Dashboard
minikube dashboard
```
#### Pod
[file db.yml](/User/pav/Documents/worka/gitRepo/k8s-specs/pod/db.yml)
```bash
kubectl run db --image mongo
# or better way
kubectl create -f ~/Documents/worka/gitRepo/k8s-specs/pod/db.yml

# logs
kubectl logs -f db

# Only kill container, bud pod immediately starts new one in pod
kubectl exec -it db pkill mongod

# Kill pod
kubectl delete -f ~/Documents/worka/gitRepo/k8s-specs/pod/db.yml
```



###### Get pod details
```bash
kubectl get pods
# and IP and Node
kubectl get pods -o wide
# NAME      READY     STATUS    RESTARTS   AGE       IP           NODE
# db        1/1       Running   0          35m       172.17.0.4   minikube
kubectl get pods -o json
kubectl get pods -o yaml
```

#### Service

###### Create services

```bash
kubectl create -f webserver-deployment.yaml


```

###### Get service list
```bash
kubectl get svc
```

###### Service info
```bash
kubectl describe svc web-service
```


###### Get number of replica 3/3 or 2/3 ...
```bash
kubectl get replicasets
```
