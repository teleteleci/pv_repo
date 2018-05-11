#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule as am

DOCUMENTATION = '''
---
module: get_environment_labels
short_description: Returns labels from inventory
'''

EXAMPLES = '''
  - name: Get environment docker labels.
    get_environment_labels:
        hostvars_env: "{{ hostvars }}"
        group_filter: "[docker_swarm_manager, docker_swarm_worker]"
    register: result
    when: inventory_hostname == groups['docker_swarm_manager'][0]
'''

RETURN = '''
host_labels:
    description: hostame list
    return: success
    type: list
    sample: ['zm01-dev17.uno.cz.infra kaf=2', 'ws01-dev17.uno.cz.infra kaf=1']
'''


# Compare two list and return true when intersection return some value
#   or return true when group_filter is empty
def is_host_in_group(group_names, group_filter):
    assert type(group_names) is list, "group_names must be list"
    assert type(group_filter) is list, "group_filter must be list"

    if group_filter == []:
        return True

    for group in group_filter:
        try:
            if 0 < len(set(group_names).intersection(set(group_filter))):
                return True
        except KeyError:
            pass

    return False


def parse_hostvars(data, group_filter):
    label_list = []
    for host in data:
        try:
            # hosts group filter
            if is_host_in_group(data[host]['group_names'], group_filter):
                for label in data[host]['labels']:
                    label_list.append(str("{} {}".format(host, label)))
        except KeyError:
            pass  # Ignore hosts without labels

    return label_list


# ansible module definition
def main():
    fields = {
        "hostvars_env": {"required": True, "type": "dict"},
        "group_filter": {"default": [], "type": "list"}
    }

    module = am(argument_spec=fields)

    response = parse_hostvars(module.params["hostvars_env"],
                              module.params["group_filter"])

    module.exit_json(changed=False,
                     host_labels=response)


if __name__ == '__main__':
    main()
