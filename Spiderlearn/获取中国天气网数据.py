#encoding:utf-8

#做网页分析的：bs4
#做网络请求的：requests

#第一步：把网页数据全部抓下来
#第二步：把抓下来的内容进行过滤，吧符合要求的内容提取出来，不需要的过滤掉

from bs4 import BeautifulSoup
import requests
import time
from pyecharts import Bar#柱状图
import operator
import json
from functools import cmp_to_key

TEMPERATURE_LIST = []
TEMPERATURE_LIST_READ = []

def Get_temperature(url):
    # 请求头，需要进行伪装
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        # 用户代理,使得服务器能够识别客户使用的操作系统及版本、CPU 类型等
        'Upgrade-Insecure-Requests': '1',
        # 不安全的请求
        # 'Referer':'http://www.weather.com.cn/textFC/db.shtml',
        # 上一个页面
        'Host': 'www.weather.com.cn'

    }
    # 使用get方式获得
    reg = requests.get(url, header)
    # reg.content获取的是二进制内容，中文需转义
    # 方法一,使用str
    # reg_utf8 = str(reg.content,'utf-8')
    # print(reg_utf8)
    # 方法二，使用requests自带encoding方法转义
    reg.encoding = 'utf-8'
    text = reg.text
    soup = BeautifulSoup(text, 'lxml')
    # 使用BeautifulSoup函数将获取到的内容用lxml引擎分析
    conMidtab = soup.find('div', class_='conMidtab')
    # 找到并返回类型是div且class为conMidtab2的第一个内容,返回的不是列表
    conMidtab2_list = conMidtab.find_all('div', class_='conMidtab2')
    # 找到并返回类型是div且class为conMidtab2的全部内容，返回为列表
    for var in conMidtab2_list:
        tr_list = var.find_all('tr')[2:]
        # 获取所有的tr并切片去掉没用的前两项
        for index, tr in enumerate(tr_list):
            # 返回列表中的第几位与内容
            if index == 0:
                # 如果是第0个tr标签，那么城市名和省份名是放在一起的
                td_list = tr.find_all('td')  # 获取所有的td
                province = td_list[0].text.replace('\n', '')
                cityname = td_list[1].text.replace('\n', '')
                min_C = td_list[7].text.replace('\n', '')
            else:
                # 如果不是第0个tr标签，那么只存放城市名
                td_list = tr.find_all('td')  # 获取所有的td
                cityname = td_list[0].text.replace('\n', '')
                min_C = td_list[6].text.replace('\n', '')

            TEMPERATURE_LIST.append({
                'city':province+cityname,
                'min_C':min_C
            })
            #print('%s|%3s' % ((province + cityname).ljust(8, u'　'), min_C))
            # 如果需要转换的元组作为转换表达式的一部分存在，
            # 那么必须将它用圆括号括起来，以避免错


def main():
    #网页的url
    urls = ['http://www.weather.com.cn/textFC/hb.shtml',
            'http://www.weather.com.cn/textFC/db.shtml',
            'http://www.weather.com.cn/textFC/hd.shtml',
            'http://www.weather.com.cn/textFC/hz.shtml',
            'http://www.weather.com.cn/textFC/hn.shtml',
            'http://www.weather.com.cn/textFC/xb.shtml',
            'http://www.weather.com.cn/textFC/xn.shtml']
    #循环爬下每个url的内容
    for i in urls:
        Get_temperature(i)
        time.sleep(2)
    #爬到的内容放到文件中
    line = json.dumps(TEMPERATURE_LIST,ensure_ascii=False)
    with open('temprature.json','wb') as fp:
        fp.write(line.encode('utf-8'))


    with open('temprature.json', 'r',encoding= 'UTF-8') as fp:
        TEMPERATURE_LIST_READ = fp.read()
        TEMPERATURE_LIST_READ = eval(TEMPERATURE_LIST_READ)

    #将爬下的内容按温度排序
    SORT_TEMPERATURE_LIST = []
    SORT_TEMPERATURE_LIST = sorted(TEMPERATURE_LIST_READ,key = lambda x:int(x['min_C']),reverse=False)
    #key每次排序时执行的函数，reverse降序

    # print(SORT_TEMPERATURE_LIST)

    #定义最小前二十城市名与其温度
    TOP20_TEM_LIST = []
    TOP20_MIN_LIST = []
    for index,va in enumerate(SORT_TEMPERATURE_LIST):
        if index <= 20:
            TOP20_MIN_LIST.append(va['min_C'])
            TOP20_TEM_LIST.append(va['city'])

    #将爬下的内容以图表显示出来
    bar = Bar(r'全国最低温度排名', '123456')  # 制定画布
    bar.add(r'地区', TOP20_TEM_LIST, TOP20_MIN_LIST)
    bar.show_config()
    bar.render(r"联网获取的最低温度排名.html")


if __name__ == '__main__':
    main()