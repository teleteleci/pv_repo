AZ_SUBSCRIPTION='ABX_DEV'
AZ_LOCTION='westeurope'
AZURE_OWNER='Pavel Vit'

FIRST_RG='pv-test-rg1'
STORAGE_LIST="[]"

az account set --subscription $AZ_SUBSCRIPTION

az group create \
    --location $AZ_LOCTION \
    --name $FIRST_RG \
    --subscription $AZ_SUBSCRIPTION \
    --tags environment=${AZURE_ENVIRONMENT_NAME} \
       owner=${AZURE_OWNER} \
       lastUpdateAt="$(date)"


az group deployment validate \
    --resource-group $FIRST_RG \
    --parameters storageList=$STORAGE_LIST \
    --template-file deployment.json

az group deployment create \
    --resource-group $FIRST_RG \
    --parameters storageList='[]' \
    --template-file deployment.json

az group deployment create \
    --resource-group $FIRST_RG \
    --parameters storageList='[{"StorageName": "pvsa12345678v9vvv1"},{"StorageName": "pvsa12345678v9vvv2"}]' \
    --template-file deployment.json
