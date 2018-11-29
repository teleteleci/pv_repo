from servicebus import Servicebus


class Queue(Servicebus):

    def __init__(self, json_definition):
        super().__init__(json_definition=json_definition)
        assert 'queue' == json_definition['objectType']
        assert json_definition['objectName'] != ''
        self.attr = self.get_default()
        self.set_atributes(data=json_definition['parameters'])
        self.template_path = 'templates/queue.json.template'

    def get_default(self):
        return {
            'queueName': self.object_name,
            'deadLetteringOnMessageExpiration': 'false',
            'defaultMessageTimeToLive': 'P14D',
            'duplicateDetectionHistoryTimeWindow': 'PT30S',
            'enableBatchedOperations': 'true',
            'enableExpress': 'false',
            'enablePartitioning': 'false',
            'lockDuration': 'PT30S',
            'maxDeliveryCount': '10',
            'maxSizeInMegabytes': '1024',
            'requiresDuplicateDetection': 'true',
            'requiresSession': 'false',
            'status': 'Active'
        }


if __name__ == '__main__':
    import json
    import os
    import queue

    os.chdir('/Users/pav/Documents/worka/gitRepo/pv_repo/python/'
             + 'playWithText/gen_AZ_SB_SeS/')

    with open('./definition/queues/testQueue.json') as f:
        data = json.load(f)

    t = queue.Queue(json_definition=data)
    print(t)
