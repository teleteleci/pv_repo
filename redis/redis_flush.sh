#!/usr/bin/env bash

# Script connect to azure and obtain redis cache primary key.
# Open contentainer with python and clean all cached information on redis.

echo -n "Type azure redis cache name like a 'abdedv-app-redis':"
read AZURE_REDIS_CACHE_NAME

echo -n "Type azure subscription like 'ABX_LIVE':"
read AZURE_SUBSCRIPTION_NAME
echo ""

az login --use-device-code
az account set --subscription ${AZURE_SUBSCRIPTION_NAME}

echo "... Obtain redis key ."
AZURE_REDIS_PRIMARY_KEY=$(az redis list-keys \
                                    -n ${AZURE_REDIS_CACHE_NAME} \
                                    -g ${AZURE_REDIS_CACHE_NAME}-rg \
                                    --query primaryKey \
                                    -o tsv)

if [ -z "$AZURE_REDIS_PRIMARY_KEY" ]; then
    echo "Can not obtain ${AZURE_REDIS_CACHE_NAME} key!"
    exit 1
fi

echo "... ${AZURE_REDIS_CACHE_NAME} will bee flushed"
echo "... run container with python script"

docker run -it \
  --name devtest \
  --env REDIS_KEY=${AZURE_REDIS_PRIMARY_KEY} \
  --env REDIS_HOST_NAME="${AZURE_REDIS_CACHE_NAME}.redis.cache.windows.net" \
  --mount type=bind,source="$(pwd)/mount_file",target=/app \
  python:3.4-alpine \
  /app/clean_redis_cache.sh
