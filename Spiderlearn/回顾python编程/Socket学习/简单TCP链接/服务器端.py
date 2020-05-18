#coding:utf-8
import socket
import threading
import time

def dealClient(sock,addr):
    #第四部：接受传来的数据，并发送给对方数据
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Hello,I am server!')
    while True:
        data = sock.recv(1024)#指定最大数据量
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        print('--->>%s!' % data.decode('utf-8'))#decode解码encode编码
        sock.send(('Loop_Msg: %s!' % data.decode('utf-8')).encode('utf-8'))
    #第五步：关闭socket
    sock.close()
    print('Connection from %s:%s closed.' % addr)

if __name__ == '__main__':
    #第一步：创建一个基于IPV4和TCP协议的socket
    #socket绑定的IP（127.0.0.1为本机IP）与端口
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #use local computer ip
    s.bind(('192.168.125.133',9996))#元组 链接wlan的地址
    #第二部：监听链接
    s.listen(5)#拒绝链接前，操作系统可以挂起的最大链接数量
    print('Waiting for Connection...')
    while True:
        #第三部：接受一个新链接
        sock,addr = s.accept()
        #创建新线程来处理Tcp链接
        t = threading.Thread(target=dealClient,args=(sock,addr))
        t.start()
