import urllib.request
import urllib.parse
url = 'https://passport.csdn.net/account/login'
#从浏览器中获取的user_agent
user_agent =  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
#从浏览器中获取的referer
referer = 'https://blog.csdn.net/'
postdata = {'username':'17864211704','password':'2650408922ww'}
headers = {'User-Agent':user_agent,'Referer':referer}
#info需要被编码为urllib.request理解的方式，这里用的是urllib.parse
#需要重新编码，不然会报错 POST data should be bytes or an iterable of bytes. It cannot be of type str.
data = urllib.parse.urlencode(postdata).encode(encoding='utf-8')
req = urllib.request.Request(url,data,headers)
response = urllib.request.urlopen(req)
html = response.read()
print(html)