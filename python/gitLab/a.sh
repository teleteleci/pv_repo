#!/usr/bin/env bash

# curl "https://gitlab.innoble.io/api/v4/projects?private_token=oZnpp9yrcDAcX1jCQhUF&per_page=100&page=2" | jq -r '[{"url":.[].http_url_to_repo, "dir":.[].namespace.full_path}]'
#
# jq -r '[{"url":.[].http_url_to_repo, "dir":.[].namespace.full_path}]' a.json
#
#
# curl "https://gitlab.innoble.io/api/v4/projects?private_token=oZnpp9yrcDAcX1jCQhUF&per_page=20&page=1" | jq -r ' .[] | select(.full_path=="Lukas.Mrtvy") | [{"url":.http_url_to_repo, "dir":.namespace.full_path, "visibility":.visibility}]'


# for GIT_REPO in $(jq -r ' .[] | select(.namespace.full_path!="Lukas.Mrtvy") | [.] | [("mkdir -p "+.[].http_url_to_repo+"; git xxx"+.[].namespace.full_path)]' \
for GIT_REPO in $(jq -r ' .[] | select(.namespace.full_path!="Lukas.Mrtvy") | [.] | ("mkdir -p "+.[].namespace.full_path+"; git clone "+.[].http_url_to_repo)' \
                  a.json); do

    # echo -n ${GIT_REPO[*]}
    # echo '   x   '

    # https://stackoverflow.com/questions/44981265/extract-json-value-to-shell-variable-using-jq
    # jq -r '@sh "export FILE=\(.file)"'
    echo "'${GIT_REPO}'"

done
