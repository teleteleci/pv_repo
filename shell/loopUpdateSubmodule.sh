#!/usr/bin/env bash

# git@gitlab.innoble.io:platform/azure-ci/abx_demo/cbs-service-bus.git

# Environments

# Constant
ENVS=(abx_live abx_demo)
OBJECT_DOMAIN=(app cbs crd crm dwh hst rsk)

cd  ~/Documents/worka/gitRepo/gitlab/azure-ci/

for env in ${ENVS[*]}; do
    echo "---------- $env ---------"
    cd $env
    for i in $(ls -d app-postgre-sql/); do
        cd ${i%%/};

        # push to git ...
        pwd
        # git submodule add ../../_common/templates/
        # git submodule add ../../_common/scripts/
        # git add .
        # git commit -am "ZERO-216 added shared_preload_libraries"
        # git pull --rebase
        # git push origin
        # git status
        # git submodule update --recursive --init --remote

        # open pipeline in browser ...
        # /Applications/Firefox.app/Contents/MacOS/firefox --new-tab https://gitlab.innoble.io/platform/azure-ci/$env/$i
        cd ..
    done
    cd ..
done
