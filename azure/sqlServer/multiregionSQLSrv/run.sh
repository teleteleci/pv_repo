#!/usr/bin/env bash

PROJECT_NAME="pv-test-sqlsrv"
AZURE_RESOURCE_GROUP=${PROJECT_NAME}
AZURE_HOME_LOCATION="westeurope"
AZURE_REMOTE_LOCATION="northeurope"
AZURE_SQL_DB_TIER="S0"

SQL_SERVER_USER='unoadmin'
SQL_SERVER_PWD='oslik_123'

az group create \
  --location $AZURE_HOME_LOCATION \
  --name $AZURE_RESOURCE_GROUP \
  --tag createdAt="$(date)" \
        owner='Starous' \
        task='https://jira.innoble.de/browse/ZERO-34#'

# create servers
az sql server create --resource-group $AZURE_RESOURCE_GROUP --admin-user ${SQL_SERVER_USER} --admin-password ${SQL_SERVER_PWD} --name ${PROJECT_NAME} --location $AZURE_HOME_LOCATION
az sql server create --resource-group $AZURE_RESOURCE_GROUP --admin-user ${SQL_SERVER_USER} --admin-password ${SQL_SERVER_PWD} --name ${PROJECT_NAME}2 --location $AZURE_REMOTE_LOCATION

# create database S0 / BC_Gen4_1
az sql db create --resource-group $AZURE_RESOURCE_GROUP --server $PROJECT_NAME --name ${PROJECT_NAME}-db --service-objective ${AZURE_SQL_DB_TIER}
# az sql db create --resource-group $AZURE_RESOURCE_GROUP --server $PROJECT_NAME --name ${PROJECT_NAME}-db --service-objective BC_Gen4_1

# Create replica
az sql db replica create -g $AZURE_RESOURCE_GROUP --server $PROJECT_NAME --name ${PROJECT_NAME}-db --partner-server "${PROJECT_NAME}2" --service-objective ${AZURE_SQL_DB_TIER}

# Create failover-Group
az sql failover-group create --resource-group $AZURE_RESOURCE_GROUP --server ${PROJECT_NAME} --partner-server "${PROJECT_NAME}2" --name ${PROJECT_NAME}-fg

# Switch primary server to 2
# az sql failover-group set-primary --name ${PROJECT_NAME}-fg --resource-group $AZURE_RESOURCE_GROUP --server "${PROJECT_NAME}2"
# az sql failover-group set-primary --name ${PROJECT_NAME}-fg --resource-group $AZURE_RESOURCE_GROUP --server "${PROJECT_NAME}"

# delete database
# az sql failover-group delete --resource-group $AZURE_RESOURCE_GROUP --server ${PROJECT_NAME} --name ${PROJECT_NAME}-fg
# az sql db delete --resource-group $AZURE_RESOURCE_GROUP --server $PROJECT_NAME --name $PROJECT_NAME-db
# az sql db delete --resource-group $AZURE_RESOURCE_GROUP --server "${PROJECT_NAME}2" --name $PROJECT_NAME-db
