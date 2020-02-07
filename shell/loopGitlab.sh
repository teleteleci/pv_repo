#!/usr/bin/env bash

# git@gitlab.innoble.io:platform/azure-ci/abx_demo/cbs-service-bus.git

# Environments
OBJECT_TYPE="aks"
GL_PREFIX='git@gitlab.innoble.io:platform/azure-ci/'

# Constant
ENVS=(abx_live abx_demo abx_dev abx_stage)
OBJECT_DOMAIN=(app crd)

cd  ~/Documents/worka/gitRepo/gitlab/azure-ci/abx_demo
# git@gitlab.innoble.io:platform/azure-ci/abx_stage/app-aks.git
for env in ${ENVS[*]}; do
    cd ../${env}
    pwd
    for obj in ${OBJECT_DOMAIN[*]};do
        echo "--- $env $obj-$OBJECT_TYPE"
        # git clone "$GL_PREFIX$env/$obj-$OBJECT_TYPE.git"
        # cp ./app-$OBJECT_TYPE/app-psql-parameters.json ./$obj-$OBJECT_TYPE/rsk-psql-parameters.json
        # cp ./app-$OBJECT_TYPE/.gitlab-ci.yml ./$obj-$OBJECT_TYPE/.gitlab-ci.yml
        cd "$obj-$OBJECT_TYPE"
        pwd
        # git submodule add ../../_common/scripts/
        # git submodule add ../../_common/templates/
        # git submodule update --recursive --init --remote
        # git add .
        # git commit -m "ZERO-257 change SQL server template dependency"
        git pull --rebase
        # git push origin
        cd ..
    done
done
