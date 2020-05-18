import urllib
import urllib.request
#请求
request = urllib.request.Request('http://www.zhihu.com')
#response = urllib.request.urlopen('http://www.zhihu.com')
#响应
response = urllib.request.urlopen(request)
html = response.read()
print(html)