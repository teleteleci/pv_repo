class Servicebus(object):

    template_path = ''

    def __init__(self, json_definition):
        self.object_type = json_definition['objectType']
        self.object_name = json_definition['objectName']
        self.data = json_definition
        self.template_path = 'templates/serviceBus.json.template'
        self.attr = ''

    def get_default():
        ret = {}
        return ret

    def set_atributes(self, data):
        for element in data:
            try:
                self.attr[element] = data[element]
            except KeyError:
                print('Uknow element: {}'.format(element))
                raise

    def __repr__(self):
        from jinja2 import Template
        with open(self.template_path) as f:
            template = Template(f.read())

        return template.render(self.attr)


if __name__ == '__main__':
    import json
    import os

    data = {
        'objectType': 'servicebus',
        'objectName': 'abx-de',
        'attr': ''
    }

    os.chdir('/Users/pav/Documents/worka/gitRepo/pv_repo/python/'
             + 'playWithText/gen_AZ_SB_SeS/')

    with open('./definition/queues/testQueue.json') as f:
        data = json.load(f)

    s = Servicebus(data)
    print(s)
