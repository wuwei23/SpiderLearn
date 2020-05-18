import pickle
d = dict(url = 'index.html',tirle = '首页',content = '首页')
print(pickle.dumps(d))#使用dumps，实现序列化
f = open(r'dump.txt','wb')
pickle.dump(d,f)#使用dump操作，将序列直接写入文件
f.close()
f1 = open(r'dump.txt','rb')
d1 = pickle.load(f1)#反序列化输出
f1.close()
print(d1)