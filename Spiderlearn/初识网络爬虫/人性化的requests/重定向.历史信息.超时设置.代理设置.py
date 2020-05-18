import requests
#将allow_redirects设为True则为允许重定向,timeout进行超时设置
r = requests.get('http://github.com',allow_redirects=True,timeout=2)
print(r.url)
print(r.status_code)
print(r.history)
#要使用正确的代理，报的错是安全警告的错，网上可以消除
proxies = {
    'http':'http://127.0.0.1:8087',
    # "http":"http://125.40.24.202:9999",
    # "https":"http://202.111.175.97:8080",
}
#verify是否验证服务器的SSL证书
requests.get("https://www.zhihu.com/",proxies=proxies,verify=False)