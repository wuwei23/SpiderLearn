import urllib.request
#Python 3 将cookielib改成 http.cookiejar了
import http.cookiejar
cookie = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
response = opener.open('http://www.zhihu.com')
for item in cookie:
    print(item.name + ':' + item.value)