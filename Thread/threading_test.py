import threading
import time
import requests


exitFlag = 0


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.url = 'http://127.0.0.1:8011/api/index/new/v4?device_id=44838D82-CA60-4438-8A02-9095BED2F67B&start_num=1&version=7.2.5'

    def run(self):
        # print('start:' + self.name)
        # threadLock.acquire()
        # print_time(self.name, self.counter, 5)
        # print('exit:' + self.name)
        # threadLock.release()
        for i in range(10):
            r = requests.get(self.url)
            print(r)


thread1 = myThread(1,'thread1', 1)
thread2 = myThread(2, 'thread2', 2)
thread3 = myThread(3, 'thread3', 2)

print('----start---')
start_time = time.time()

thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()

print('exit')

print('end-----')
print(time.time() - start_time)
