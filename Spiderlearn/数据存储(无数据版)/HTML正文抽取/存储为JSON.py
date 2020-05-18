#coding=utf-8
import json
import requests
from bs4 import BeautifulSoup
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0'
headers = {'User-Agent':user_agent}
r = requests.get('http://seputu.com/',headers=headers)
r.encoding = 'utf-8'#修改编码方式
#print(r.text)
soup = BeautifulSoup(r.text,'html.parser')
content = []
for mulu in soup.find_all(class_ = "mulu"):
    h2 = mulu.find('h2')
    if h2 != None:
        h2_title = h2.string #获取标题
        list_ = []
        for a in mulu.find(class_='box').find_all('a'):#获取所有a标记中url和章节内容
            href = a.get('href')
            box_title = a.get('title')
            list_title = box_title.split('_')
            box_title = list_title[0]
            # print(href,box_title[21:])
            list_.append({'href':href,'box_title':box_title[21:]})
        content.append({'title':h2_title,'content':list_})
with open('盗墓笔记章节名与链接.json','w') as fp:
    json.dump(content,fp=fp,indent=4)