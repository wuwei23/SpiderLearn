import urllib.request
proxy = urllib.request.ProxyHandler({'http':'127.0.0.1:8087'})
opener = urllib.request.build_opener(proxy)
# urllib.request.install_opener(opener)#全局代理设置
# response = urllib.request.urlopen('https://www.zhihu.com/')
response = opener.open("https://www.zhihu.com/")
print(response.read())