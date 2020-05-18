import requests
#get请求
r = requests.get('http://www.baidu.com')
#post请求
postdata = {'username':'17864211704','password':'2650408922ww'}
r = requests.post('https://passport.csdn.net/account/login',data=postdata)
#复杂的url如https://zzk.cnblogs.com/s/blogpost?keywords=blog%3Aqiyeboy&pageindex=1
payload = {'keywords':'blog:qiyeboy','pageindex':1}
r = requests.get('http://zzk.cnblogs.com/s/blogpost',params=payload)
print(r.url)