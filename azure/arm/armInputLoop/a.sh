#!/usr/bin/env bash

# Parent project environments
AZURE_SUBSCRIPTION_NAME='ABX_STAGE'
AZURE_RESOURCE_NAME_PREFIX='abdesg'
AZURE_PRIMARY_LOCATION='westeurope'
AZURE_ENVIRONMENT_NAME='Stage'

if [ -z $AZURE_SUBSCRIPTION_NAME ] || [ -z $AZURE_RESOURCE_NAME_PREFIX ]; then
    echo "Error: Subscription name and resource name prefix is mandatory !"
    exit 1
fi

# Change it
AZURE_PARAMETERS_FILENAME="pv-svcbus-parameters.json"
AZURE_OWNER="STAGE_ADMINS"

# Constant
AZURE_DOMAIN=$(jq -r '.parameters.serviceBus.value.domain' $AZURE_PARAMETERS_FILENAME)
AZURE_DEPLOYMENT_PREFIX="${AZURE_RESOURCE_NAME_PREFIX}-$AZURE_DOMAIN-svcbus-deployment"
AZURE_RESOURCE_GROUP="${AZURE_RESOURCE_NAME_PREFIX}-$AZURE_DOMAIN-svcbus-rg"
AZURE_TEMPLATE_FILENAME="./templates/svcbus-template.json"
AZURE_PARAMETERS_FILENAME="$AZURE_DOMAIN-svcbus-parameters.json"
GITLAB_DEPLOY_BRANCH="master"

if [ -z $AZURE_DOMAIN ]; then
    echo "Error: Domain must be defined at parameter file $AZURE_PARAMETERS_FILENAME !"
    exit 1
fi

# az login --use-device-code
az account set --subscription $AZURE_SUBSCRIPTION_NAME

az group create \
  --name ${AZURE_RESOURCE_GROUP} \
  --location ${AZURE_PRIMARY_LOCATION} \
  --subscription ${AZURE_SUBSCRIPTION_NAME} \
  --tags environment=${AZURE_ENVIRONMENT_NAME} \
         owner=${AZURE_OWNER} \
         pipeline=${CI_REPOSITORY_URL} \
         lastUpdatedAt="$(date)" \
  --verbose

az group deployment validate \
  --resource-group ${AZURE_RESOURCE_GROUP} \
  --template-file ${AZURE_TEMPLATE_FILENAME} \
  --parameters @${AZURE_PARAMETERS_FILENAME} \
               resourceNamePrefix=${AZURE_RESOURCE_NAME_PREFIX} \
               environment=${AZURE_ENVIRONMENT_NAME} \
               owner=${AZURE_OWNER} \
  --subscription ${AZURE_SUBSCRIPTION_NAME} \
  --mode Incremental \
  --verbose


  az group deployment create \
    --resource-group ${AZURE_RESOURCE_GROUP} \
    --template-file ${AZURE_TEMPLATE_FILENAME} \
    --parameters @${AZURE_PARAMETERS_FILENAME} \
                 resourceNamePrefix=${AZURE_RESOURCE_NAME_PREFIX} \
                 environment=${AZURE_ENVIRONMENT_NAME} \
                 owner=${AZURE_OWNER} \
    --subscription ${AZURE_SUBSCRIPTION_NAME} \
    --mode Incremental \
    --verbose
