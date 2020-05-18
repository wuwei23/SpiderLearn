import urllib.request
import urllib.parse
url = 'https://passport.csdn.net/account/login'
postdata = {'username':'17864211704','password':'2650408922ww'}
#info需要被编码为urllib.request理解的方式，这里用的是urllib.parse
#需要重新编码，不然会报错 POST data should be bytes or an iterable of bytes. It cannot be of type str.
data = urllib.parse.urlencode(postdata).encode(encoding='utf-8')
req = urllib.request.Request(url,data)
response = urllib.request.urlopen(req)
html = response.read()
print(html)