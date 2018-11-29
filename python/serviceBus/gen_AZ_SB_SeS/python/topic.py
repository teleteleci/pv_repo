from servicebus import Servicebus


class Topic(Servicebus):

    def __init__(self, json_definition):
        super().__init__(json_definition=json_definition)
        assert 'topic' == json_definition['objectType']
        assert json_definition['objectName'] != ''
        self.attr = self.get_default()
        self.set_atributes(data=json_definition['parameters'])
        self.template_path = 'templates/topic.json.template'

    def get_default(self):
        return {
            'topicName': self.object_name,
            'autoDeleteOnIdle': 'P1D',
            'defaultMessageTimeToLive': 'P14D',
            'duplicateDetectionHistoryTimeWindow': 'PT30S',
            'enableBatchedOperations': 'true',
            'enableExpress': 'false',
            'enablePartitioning': 'false',
            'maxSizeInMegabytes': '1024',
            'requiresDuplicateDetection': 'true',
            'status': 'Active',
            'supportOrdering': 'true'
        }


if __name__ == '__main__':
    import json
    import os
    import topic

    os.chdir('/Users/pav/Documents/worka/gitRepo/pv_repo/python/'
             + 'playWithText/gen_AZ_SB_SeS/')

    with open('./definition/topics/testTopic.json') as f:
        data = json.load(f)

    t = topic.Topic(json_definition=data)
    print(t)
