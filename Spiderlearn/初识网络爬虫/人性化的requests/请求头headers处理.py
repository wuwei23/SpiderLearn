import requests
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
headers = {'User-Agent':user_agent}
r = requests.get('http://www.baidu.com',headers=headers)
print(r.content)