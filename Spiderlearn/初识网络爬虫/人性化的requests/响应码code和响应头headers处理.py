import requests
r = requests.get('http://www.baidu.com')
if r.status_code == requests.codes.ok:
    print(r.status_code)#响应码
    print(r.headers)#响应头
    print(r.headers.get('content-type'))#推荐使用这种获取方式，获取其中的某个字段
    print(r.headers['content-type'])#不推荐使用这种获取方式
else:
    r.raise_for_status()

#上述程序中，r.headers包含所有的响应头信息，可以通过get函数获取其中的
#某一个字段，也可以通过字典引用的方式获取字典值，但是不推荐，因为如果字段中没有这个字段
#第二种方式会抛出异常，第一种方式会返回None。 r.raise_for_status()是
#用来主动的产生一个异常，当响应码是4XX或5XX时， r.raise_for_status()函数会抛出
#异常，而当响应码为200时， r.raise_for_status()函数会返回None