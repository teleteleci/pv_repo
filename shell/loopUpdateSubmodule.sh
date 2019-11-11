#!/usr/bin/env bash

# git@gitlab.innoble.io:platform/azure-ci/abx_demo/cbs-service-bus.git

# Environments

# Constant
ENVS=(abx_stage abx_demo abx_live abx_dev)

cd  ~/Documents/worka/gitRepo/gitlab/azure-ci/

for env in ${ENVS[*]}; do
    echo "---------- $env ---------"
    cd $env
    for i in $(ls -d sch-sqlserver/); do
        cd ${i%%/};

        # push to git ...
        pwd
        # git commit -am "ZERO-97 new CRM sql server db"
        # git pull --rebase
        # git push origin
        # git status
        # git submodule add ../../_common/templates/
        # git submodule add ../../_common/scripts/
        # git submodule update --recursive --init --remote
        # git add .
        # git commit -m "zero-136 New sql server and db 'sch'"
        # git push origin

        # open pipeline in browser ...
        # /Applications/Firefox.app/Contents/MacOS/firefox --new-tab https://gitlab.innoble.io/platform/azure-ci/$env/$i
        cd ..
    done
    cd ..
done
