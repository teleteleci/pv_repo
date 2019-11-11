#!/usr/bin/env bash

# git@gitlab.innoble.io:platform/azure-ci/abx_demo/cbs-service-bus.git

# Environments
OBJECT_TYPE="sqlserver"
GL_PREFIX='git@gitlab.innoble.io:platform/azure-ci/'

# Constant
ENVS=(abx_live abx_demo abx_stage abx_dev)
OBJECT_DOMAIN=(sch)

cd  ~/Documents/worka/gitRepo/gitlab/azure-ci/abx_demo

for env in ${ENVS[*]}; do
    cd ../${env}
    pwd
    for obj in ${OBJECT_DOMAIN[*]};do
        echo "--- $env $obj-$OBJECT_TYPE"
        # git clone "$GL_PREFIX$env/$obj-$OBJECT_TYPE.git"
        # cd "$OBJECT_DOMAIN-$OBJECT_TYPE"
        # git submodule add ../../../_common/scripts/
        # git submodule add ../../../_common/templates/
        # git submodule update --recursive --init --remote
        # cd ..
    done
done
