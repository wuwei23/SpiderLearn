import requests

#获取cookie字段的值
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
headers = {'User-Agent':user_agent}
r = requests.get('http://www.baidu.com',headers=headers)
#遍历出所有的cookie字段
for cookie in r.cookies.keys():
    print(cookie + ':' + r.cookies.get(cookie))


#自定义cookie的值发送出去
cookies = dict(name='qiye',age='10')
r = requests.get('http://www.baidu.com',headers=headers,cookies=cookies)
print(r.text)


#自动处理cookie的方式
loginUrl = 'https://passport.csdn.net/account/login'
s = requests.Session()
#首先访问登陆界面，作为游客，服务器会先分配一个cookie
r = s.get(loginUrl,allow_redirects=True)
dates = {'username':'17864211704','password':'2650408922ww'}
#向登陆连接发送post请求，验证成功，游客权限转为会员权限
r = s.post(loginUrl,data=dates,allow_redirects=True)
print(r.text)

#如果没有第一步访问登录的页面，而是直接向登陆链接发送post请求，
# 系统会把你当作非法用户，因为访问登陆界面时会分配一个cookie，
# 需要将这个cookie在发送post请求时带上，这种使用session函数
#处理cookie的方式以后会很常用