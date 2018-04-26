#!/usr/bin/python

import requests
import re
import json
import datetime
from ansible.module_utils.basic import *


DATE_FORMAT = "%Y-%m-%d"


def get_ans_input(data, rslt):
    option = {"auth": (data['jira_user'], data['jira_pwd']),
              "url": data['jira_rest_url'] + "/rest/api/2",
              "project": data['project_name'],
              "release": data['release_name']}
    return option[rslt]


# get date in specific format
def get_current_date():
    return datetime.datetime.strftime(datetime.date.today(), DATE_FORMAT)


def get_current_release_info(auth, project, url, release_name):
    try:
        response = requests.get(url + "/project/" + project + "/versions",
                                auth=auth)

        # print(sys.version)
        if(response.ok):
            r = map(lambda x: x,
                    filter(lambda js:
                           # not released yet
                           not js["released"]
                           # and release name is in correct format
                           and str(js["name"]).find(release_name) == 0,
                           response.json()))
            rl = list(r)
            assert len(rl) == 1, \
                "The one release must exists only! found = {}" \
                .format(len(rl))
            rslt = rl[0]
        else:
            response.raise_for_status()
    except Exception as e:
        # print("Could not call {}, with response {}".format(url, response))
        raise
    return rslt


def create_new_release(release_name, auth, project, url):
    try:
        rq_data = json.dumps({
            "name": release_name,
            "description": "auto-generated",
            "startDate": get_current_date(),
            "project": project
        })
        # print(rq_data)

        response = requests.post(
            url=url + "/version",
            data=rq_data,
            auth=auth,
            headers={"Content-Type": "application/json"})

        if(response.ok):
            pass
            # print(response.json())
        else:
            print("response.headers - {}".format(response.headers))
            print("response - {}".format(response.text))
            response.raise_for_status()

    except Exception as e:
        # print("Could not call {}, with response {}".format(url, response))
        raise
    return response.json()


def get_next_release_name(current_release_name, release_name):
    regex_mask = "^(" + release_name + "-" + "[0-9]*\.[0-9]*\.){1}([0-9]*)$"
    regex = re.search(regex_mask, current_release_name)
    return regex.group(1) + str(int(regex.group(2)) + 1)


def mark_released(url, new_release, auth):
    try:
        rq_data = json.dumps({
            "released": "true",
            "releaseDate": get_current_date(),
            "expand": "operations",
            "moveUnfixedIssuesTo": str(new_release)})
        # print(rq_data)

        response = requests.put(
            url=url,
            data=rq_data,
            auth=auth,
            headers={"Content-Type": "application/json"})

        if(response.ok):
            pass
            # print(response.json())
        else:
            print("response.headers - {}".format(response.headers))
            print("response - {}".format(response.text))
            response.raise_for_status()

    except Exception as e:
        print("Could not call {}, with response {}".format(url, response))
        raise
    return response.json()


# ansible module definition
def main():
    fields = {
        "jira_user": {"required": True, "type": "str"},
        "jira_pwd": {"required": True, "type": "str"},
        "jira_rest_url": {"required": True, "type": "str"},
        "project_name": {"required": True, "type": "str"},
        "release_name": {"required": True, "type": "str"}
    }

    module = AnsibleModule(argument_spec=fields)

    origin_release = get_current_release_info(
        get_ans_input(module.params, "auth"),
        get_ans_input(module.params, "project"),
        get_ans_input(module.params, "url"),
        get_ans_input(module.params, "release"))

    new_release = create_new_release(
        get_next_release_name(
            origin_release['name'],
            get_ans_input(module.params, "release")),
        get_ans_input(module.params, "auth"),
        get_ans_input(module.params, "project"),
        get_ans_input(module.params, "url"))

    mark_released(origin_release['self'],
                  new_release['id'],
                  get_ans_input(module.params, "auth"))

    response = {"Origin_release": origin_release['name'],
                "New_release": new_release['name']}

    module.exit_json(changed=False, meta=response)


if __name__ == '__main__':
    main()