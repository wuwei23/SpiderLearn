import threading
mylock = threading.RLock()
#Lock与RLock都可以对线程进行加锁，区别是Lock中一个线程运行多次acquire(获取)操作
#会阻塞，而RLock不会
num = 0
class myThread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self,name=name)

    def run(self):
        global num
        while True:
            mylock.acquire()#获取锁操作
            print('%s locked,Number: %d' % (threading.current_thread().name,num))
            if num >= 4:
                mylock.release()#释放锁操作
                print('%s released,Number: %d' % (threading.current_thread().name,num))
                break
            num+=1
            print('%s released,Number: %d' % (threading.current_thread().name,num))
            mylock.release()


if __name__ == '__main__':
    thread1 = myThread('Thread1')
    thread2 = myThread('Thread2')
    thread1.start()
    thread2.start()

#先运行线程1，对num加锁 ，使num一直属于线程1，知道num=4，线程一结束
# 运行线程2，此时num值为4，只运行一次结束