import multiprocessing
import random
import os,time

#Pip方法返回（conn1，conn2）代表一个管道的亮度啊女，Pipe方法有duplex参数，
# 如果duplex参数值为True（默认值），那么代表这个管道为全双工模式，若duplex
#值为False，conn1只负责接收消息，conn2只负责发送消息，send和recv方法分别是
# 发送和接收消息的方法，如果没有消息可以接收，recv方法会已知阻塞，如果管道已经关闭
#recv会抛出EOPError

def proc_send(pipe,urls):
    for url in urls:
        print('Process(%s) send: %s' % (os.getpid(),url))
        pipe.send(url)
        time.sleep(random.random())#生成一个0~1的随机浮点数

def proc_recv(pipe):
    while True:
        print('Process(%s) rev:%s' % (os.getpid(),pipe.recv()))
        time.sleep(random.random())

if __name__ == "__main__":
    pipe = multiprocessing.Pipe()#创建一个管道
    p1 = multiprocessing.Process(target=proc_send,args=(pipe[0],
            ['url_'+str(i) for i in range(10)]))
    p2 = multiprocessing.Process(target=proc_recv,args=(pipe[1],))
    p1.start()
    p2.start()
    p1.join()
    p2.join()