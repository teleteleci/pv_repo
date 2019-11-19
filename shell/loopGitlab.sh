#!/usr/bin/env bash

# git@gitlab.innoble.io:platform/azure-ci/abx_demo/cbs-service-bus.git

# Environments
OBJECT_TYPE="postgre-sql"
GL_PREFIX='git@gitlab.innoble.io:platform/azure-ci/'

# Constant
ENVS=(abx_demo abx_stage abx_live)
OBJECT_DOMAIN=(rsk)

cd  ~/Documents/worka/gitRepo/gitlab/azure-ci/abx_demo

for env in ${ENVS[*]}; do
    cd ../${env}
    pwd
    for obj in ${OBJECT_DOMAIN[*]};do
        echo "--- $env $obj-$OBJECT_TYPE"
        # git clone "$GL_PREFIX$env/$obj-$OBJECT_TYPE.git"
        # cp ./app-$OBJECT_TYPE/app-psql-parameters.json ./$obj-$OBJECT_TYPE/rsk-psql-parameters.json
        # cp ./app-$OBJECT_TYPE/.gitlab-ci.yml ./$obj-$OBJECT_TYPE/.gitlab-ci.yml
        cd "$obj-$OBJECT_TYPE"
        # pwd
        # git submodule add ../../_common/scripts/
        # git submodule add ../../_common/templates/
        git submodule update --recursive --init --remote
        git add .
        git commit -m "ZERO-243 new rsk Postgre SQL server"
        git pull --rebase
        git push origin
        cd ..
    done
done
