#coding:utf-8
#TCP通信需要建立一个可靠的链接，而且 通信双方以流的形式发送数据。相对与TCP，
# UDP则是面向无连接的协议。使用UDP时，不需要建立连接，
# 只需要知道对方的IP地址和端口号，就可以直接发送数据包，速度快但不可靠

import socket
#创建Socket，绑定指定的IP和端口
#SOCK_DGRAM指定了这个socket的类型是UDP，绑定端口和TCP示例一样
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9999))
print('Bind UDP on 9999')
while True:
    #直接发送数据和接受数据
    data,addr = s.recvfrom(1024)
    print('Received from %s:%s' % addr)
    s.sendto(b'Hello, %s!' % data,addr)
