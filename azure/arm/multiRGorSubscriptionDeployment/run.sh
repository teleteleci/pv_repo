AZ_SUBSCRIPTION='ABX_DEV'
AZ_LOCTION='westeurope'

FIRST_RG='pv-test-rg1'
SECOND_RG='pv-test-rg2'

az account set --subscription $AZ_SUBSCRIPTION

az group create \
    --location $AZ_LOCTION \
    --name $FIRST_RG \
    --subscription $AZ_SUBSCRIPTION

az group create \
    --location $AZ_LOCTION \
    --name $SECOND_RG \
    --subscription $AZ_SUBSCRIPTION

az group deployment validate \
    --resource-group $FIRST_RG \
    --parameters secondResourceGroup=$SECOND_RG \
    --template-file deployment.json

az group deployment create \
    --resource-group $FIRST_RG \
    --parameters secondResourceGroup=$SECOND_RG \
    --template-file deployment.json
