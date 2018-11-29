#!/bin/bash
NAMESPACE='abx-de'
RESOURCEGROUP='abx-de-service-bus-rg'

getApList() {
    echo '    "accessPolicies": '$(az servicebus topic authorization-rule list \
        --resource-group $RESOURCEGROUP  \
        --namespace-name $NAMESPACE \
        --topic-name $1 \
        --query [].rights\
        --output json)','
}

getSubsciptionList() {
    echo '    "subscriptions": '$(az servicebus topic subscription list \
    --resource-group $RESOURCEGROUP  \
    --namespace-name $NAMESPACE \
    --topic-name $1 \
    --query [].name\
    --output json
    )
}

getTopic() {
    topic=$1
    echo '{'
    echo '    "objectType": "topic",'
    echo '    "objectName": "'$1'",'
    echo '    "parameters": {},'
    getApList $topic
    getSubsciptionList $topic
    echo '}'
}

for topic in $(az servicebus topic list \
    --resource-group $RESOURCEGROUP \
    --namespace-name $NAMESPACE \
    --query [].name -o tsv)
do
    echo 'generate topic '$topic' in progress ...'
    getTopic $topic > '../definition/topics/topic-'$topic'.json'
done
