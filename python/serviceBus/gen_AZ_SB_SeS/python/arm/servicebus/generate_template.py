from servicebus import Servicebus
from topic import Topic
from queue import Queue
from authorizationRules import AuthorisationRules
from subscriptions import Subscriptions
import json
import os
from jinja2 import Template


def get_sb_resource():
    data = {
        'objectType': 'servicebus',
        'objectName': 'abx-de',
        'attr': ''
    }
    s = Servicebus(data)
    return '{}'.format(s)


def get_queue_resource(input_file_path):
    ret = ''
    with open(input_file_path) as f:
        qdata = json.load(f)
    q = Queue(qdata)
    ret += '{}{}'.format(
        q,
        AuthorisationRules(q)
    )
    return ret


def get_topic_resource(input_file_path):
    ret = ''
    with open(input_file_path) as f:
        tdata = json.load(f)
    t = Topic(tdata)
    ret += '{}{}{}'.format(
        t,
        AuthorisationRules(t),
        Subscriptions(t)
    )
    return ret


def sort_list(unsorted_list):
    unsorted_list.sort()
    return unsorted_list


if __name__ == '__main__':
    # setup working directory
    os.chdir('../.')
    home_dir = os.getcwd()

    # generate servicebus
    src = get_sb_resource()

    # generate all topics
    for topic_file in \
            sort_list(os.listdir(home_dir + '/definition/topics')):
        src += get_topic_resource('./definition/topics/' + topic_file)

    # generate all queues
    for queue_file in \
            sort_list(os.listdir(home_dir + '/definition/queues/')):
        src += get_queue_resource('./definition/queues/' + queue_file)

    with open('./templates/serviceBus-template.json') as f:
        template = Template(f.read())

    f = open("sb-templates-gen.json", "w")
    f.write(template.render(resources=src))
    f.close()
