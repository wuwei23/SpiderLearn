import random,time,queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
#任务个数
task_number = 10
#第一步，建立task_queue和result_queue，用来存放任务和结果
task_queue = queue.Queue(task_number)
result_queue = queue.Queue(task_number)
def get_task():
    return task_queue
def get_result():
    return result_queue

#创建队列管理的类
class Queuemanager(BaseManager):
    pass

def win_run():
    #第二部：把创建的两个队列注册在网络上，利用register方法，callable参数关联Queue对象，
    #将Queue对象在网络中暴露,它们用来进行进程间通信，交换对象
    #Windows下绑定调用接口不能使用lambda，所以只能先定义函数再绑定
    Queuemanager.register('get_task_queue',callable=get_task)
    Queuemanager.register('get_result_queue',callable=get_result)

    #第三部：绑定端口 8001，设置验证口令'qiye',这个相当于对象的初始化
    # windows需要写ip地址
    manager = Queuemanager(address=('127.0.0.1',8001),authkey=b'qiye')

    #第四部：启动管理，监听信息通道
    manager.start()
    try:
        #第五步：通过管理实例的方法获得通过网络访问的Queue对象
        task = manager.get_task_queue()
        result = manager.get_result_queue()

        #第六步：添加任务
        for url in ["ImageUrl_" + str(i) for i in range(10)]:
            print('put task %s ...' % url)
            task.put(url)#
        #获取返回结果
        print('try get result...')
        for i in range(10):
            print('result is %s' % result.get(timeout =  10))#超时限制
    except:
        print('Manage Error')
    finally:
        #关闭管理
        manager.shutdown()

if __name__ == '__main__':
    #windows下多进程可能会有问题，添加这句可以缓解
    freeze_support()
    win_run()


#总结：首先创建好队列（任务队列与结果队列），其次创建好队列管理类以此来操纵分布式数据传输