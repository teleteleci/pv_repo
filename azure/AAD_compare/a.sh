!/usr/bin/env bash

# environments
AZURE_SUBSCRIPTION="ABX_DEMO"
AZURE_ROLE="central_all_on_call"

# constants
AZURE_RESOURCE_LIST=(abdelv-app-sqlsrv abdelv-crd-sqlsrv abdelv-dwh-sqlsrv abdelv-hst-sqlsrv abdelv-rsk-sqlsrv)


# Set subcription
az account set -s ${AZURE_SUBSCRIPTION}

for resource in ${AZURE_RESOURCE_LIST[*]}; do
    echo ${resource}
    # az ad group member list --group ${AZURE_ROLE} --query [].displayName

done




# dbAdminsAadRole
