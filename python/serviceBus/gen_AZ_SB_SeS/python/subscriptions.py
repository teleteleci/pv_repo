from servicebus import Servicebus


class Subscriptions(Servicebus):

    def __init__(self, object):
        super().__init__(json_definition=object.data)
        self.template_path = './templates/subscription.json.template'
        try:
            self.subscriptions = self.data['subscriptions']
        except KeyError:
            print('Topic {} has no subscriptions.'.format(self.topicName))
            self.subscriptions = []

    def get_default(self, topicName, subscriptionName):
        return {
            'subscriptionName': subscriptionName,
            'topicName': topicName,
            'deadLetteringOnMessageExpiration': 'false',
            'defaultMessageTimeToLive': 'P14D',
            'enableBatchedOperations': 'true',
            'lockDuration': 'PT30S',
            'status': 'Active'
        }

    def __repr__(self):
        from jinja2 import Template

        with open(self.template_path) as f:
            template = Template(f.read())

        subscriptions = ''
        for sub in self.subscriptions:
            attr = self.get_default(
                topicName=self.object_name,
                subscriptionName=sub)
            subscriptions += template.render(attr)
        return subscriptions


if __name__ == '__main__':
    import json
    import subscriptions
    from topic import Topic

    with open('./definition/topics/testTopic.json') as f:
        data = json.load(f)

    t = Topic(data)
    s = subscriptions.Subscriptions(t)
    print(s)
