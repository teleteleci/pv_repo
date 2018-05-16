from etcd import Client
from etcd import EtcdKeyNotFound

# constants definition
ETCD_RESULT = 'etcdResult'
IS_NODE_AT_ETCD = 'isNodeAtEtcd'
ETCD_KEY = 'key'
ETCD_VALUE = 'value'

missingNode = []
nodeAtEtcd = dict()


# def getValue(etcdClient, node):
#     isNodeAtEtcd = False
#     etcdValue = ''
#
#     try:
#         etcdValue = etcdClient.get(node).value
#         isNodeAtEtcd = True
#     except EtcdKeyNotFound:
#         print('.... Warning node ', node, ' not exists')
#         isNodeAtEtcd = False
#
#     return {ETCD_KEY: node,
#             ETCD_VALUE: etcdValue,
#             IS_NODE_AT_ETCD: isNodeAtEtcd}


# def addNodeToArray(etcdResult):
#     if etcdResult[IS_NODE_AT_ETCD]:
#         print(True)
#         nodeAtEtcd[etcdResult[ETCD_KEY]
#                    ] = etcdResult[ETCD_VALUE]
#     else:
#         print(False)
#         missingNode.append(etcdResult[ETCD_KEY])


cl = Client(host='10.130.172.114', port=4001)
cl.set('/nodes/n6', 6)

# addNodeToArray(getValue(cl, '/c/d'))
# print(getValue(cl, '/c/d'))

# addNodeToArray(getValue(cl, '/nodes/n7'))
# addNodeToArray(getValue(cl, '/nodes/n6'))

# print('----------------- not at etcd -----------------')
# print(missingNode)
# for i in missingNode:
#     print(i)
#
# print('----------------- at etcd -----------------')
# for key, value in nodeAtEtcd.items():
#     print(key, '--> ', value)
