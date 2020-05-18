import random
import threading
import time

#线程类，重写__init__与run方法
class myThread(threading.Thread):
    def __init__(self,name,urls):
        threading.Thread.__init__(self,name=name)
        self.urls = urls

    def run(self):
        print('Current %s is running...' % threading.current_thread().name)
        for url in self.urls:
            print('%s--->>> %s' % (threading.current_thread().name,url))
            time.sleep(random.random())
        print('%s is ended.' % threading.current_thread().name)


print('Current %s is running...' % threading.current_thread().name)
t1 = myThread(name='Thread1',urls=['url_1','url_2','url_3'])
t2 = myThread(name='Thread2',urls=['url_4','url_5','url_6'])
t1.start()
t2.start()
t1.join()
t2.join()
print('%s is ended.' % threading.current_thread().name)