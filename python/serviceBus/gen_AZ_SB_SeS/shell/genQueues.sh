#!/bin/bash
NAMESPACE='abx-de'
RESOURCEGROUP='abx-de-service-bus-rg'

getAP() {
    echo '    "accessPolicies": '$(az servicebus queue authorization-rule list \
        --resource-group $RESOURCEGROUP  \
        --namespace-name $NAMESPACE \
        --queue-name $1 \
        --query [].rights\
        --output json)
}

getQueue() {
    queue=$1
    echo '{'
    echo '    "objectType": "queue",'
    echo '    "objectName": "'$1'",'
    echo '    "parameters": {}',
    getAP $queue
    echo '}'
}

# cd ../queue

for queue in $(az servicebus queue list \
    --resource-group $RESOURCEGROUP \
    --namespace-name $NAMESPACE\
    --query [].name -o tsv)
do
    echo 'generate queue '$queue'.json in progress ...'
    getQueue $queue > '../definition/queues/queue-'$queue'.json'
done
