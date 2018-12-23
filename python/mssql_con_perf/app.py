import threading
import time
import create_conn as cc
from random import randint


number_of_threads = 1000
max_connection_open_time = 500
rotation_in_threat = 3

exitFlag = 0
thread_list = []
sql = 'SELECT count(1) FROM sys.dm_exec_sessions AS sess' \
    + ' JOIN sys.dm_exec_connections AS conn' \
    + ' ON sess.session_id = conn.session_id'


class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        print_time(self.name, self.counter, rotation_in_threat)
        print("Exiting " + self.name)


def print_time(threadName, delay, counter):
    print("%s: started" % (threadName))
    while counter:
        if exitFlag:
            threadName.exit()
        cc.exec_single_query(sql=sql,
                             idle_time=randint(0, max_connection_open_time),
                             thread_name=threadName)
        time.sleep(delay)
        counter -= 1


# Create new threads
for i in range(number_of_threads):
    t = myThread(i+1, "Thread-{}".format(i+1), 10)
    thread_list.append(t)

# Start new Threads
for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Exiting Main Thread")
