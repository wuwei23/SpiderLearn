from multiprocessing import Pool
import os,time,random

def run_task(name):
    print('Task %s (pid = %s) is running...' % (name,os.getpid()))
    time.sleep(random.random() * 3)
    print('Task %s end.' % name)

if __name__ == '__main__':
    print('Current process %s.' % os.getpid())
    p = Pool(processes=3)
    #三个进程大小的进程池，当有新的请求提交到Pool时，如果池还没有满，那么
    #就会创建一个新的进程用来执行该请求，如果池中的进程数已经达到规定最大值，
    #那么该请求就会等待，直到池中有进程结束，才会创建新的进程来处理它。
    for i in range(5):
        p.apply_async(run_task,args=(i,))
        #当一个函数的参数存在于一个元组或者一个字典中时，
        # 用来间接的调用这个函数，
        # 并肩元组或者字典中的参数按照顺序传递给参数
    print('Waiting for all subprocesses done...')
    p.close()#关闭进程池
    p.join()
    print('All subprocesses done.')