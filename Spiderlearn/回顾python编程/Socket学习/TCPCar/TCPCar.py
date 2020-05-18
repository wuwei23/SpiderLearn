#coding:utf-8
import socket
#初始化Socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#链接目标的IP和端口
s.connect(('192.168.1.1',2001))
#发送消息
s.send(b'\xFF\x00\x01\x00\xFF')
#print('-->>'+s.recv(1024).decode('utf-8'))
#关闭socket
s.close()