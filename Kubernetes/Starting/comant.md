# Kubernetes

## Comands

#### Dashboard

###### run dashboard
```bash
minikube dashboard
```

#### Service

###### Create services

```bash
kubectl create -f webserver.yaml
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
