#使用urlretrieve()方法直接下载远程数据到本地
import urllib.request
from bs4 import BeautifulSoup
import requests
def Schedule(blocknum,blocksize,totalsize):
    """
    :param blocknum: 已经下载的数据块
    :param blocksize: 数据块的大小
    :param totalsize: 远程文件的大小
    :return:
    """
    per = 100.0 * blocknum * blocksize / totalsize
    if per > 100:
        per = 100
    print('当前下载进度：%d' % per)

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0'
headers = {'User-Agent':user_agent}
r = requests.get('http://www.ivsky.com/tupian/ziranfengguang/',headers=headers)
r.encoding = 'utf-8'#修改编码方式
#print(r.text)
soup = BeautifulSoup(r.text,'html.parser')
img_urls = soup.find_all('img')
# print(img_urls)
i = 0
for img_url in img_urls:
    img_url = str(img_url)
    img_url = img_url.split('"')[3]
    # print(img_url)
    urllib.request.urlretrieve(img_url,'img'+str(i) +'.jpg',Schedule)
    i += 1