from bs4 import BeautifulSoup
import requests

#请求头，需要进行伪装
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    #用户代理,使得服务器能够识别客户使用的操作系统及版本、CPU 类型等
    'Upgrade-Insecure-Requests':'1',
    #不安全的请求
    'Referer':'http://www.17k.com/book/2743300.html',
    #上一个页面
    'Host':'www.17k.com'

}
#使用get方式获得
reg = requests.get('http://www.17k.com/list/2743300.html',header)
reg.encoding = 'utf-8'
text = reg.text
soup = BeautifulSoup(text,'lxml')
dd = soup.find_all('dd')
print(dd[7].text.replace(' ',''))