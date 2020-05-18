import urllib.request
opener = urllib.request.build_opener()
opener.addheaders.append(('Cookie','email=' + "2650408922@qq.com"))
req = urllib.request.Request("http://www.zhihu.com/")
response = opener.open(req)
print(response.headers)
retdata = response.read()
