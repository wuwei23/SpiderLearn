import os
from multiprocessing import Process
#子进程要执行的代码
def run_proc(name):
    print('Child process %s (%s) Running...' % (name,os.getpid()))
if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    for i in range(5):
        p = Process(target=run_proc,args=(str(i),))#创建进程，args:该函数的参数，需要使用tuple
        print('Process will start.')
        p.start()#start启动进程
    p.join()#join实现进程间的同步，可以理解为阻塞当前进程
    print('Process end.')