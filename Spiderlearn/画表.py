from pyecharts import Bar#柱状图
import sys

TEMPERATURE_LIST = ""
TOP20_TEM_LIST = []
TOP20_MIN_LIST = []
with open('temprature.json', 'r',encoding='utf-8') as fp:
    TEMPERATURE_LIST = fp.read()
    TEMPERATURE_LIST = eval(TEMPERATURE_LIST)#重点,在这里将str类型的还原为list与dict类型
    TEMPERATURE_LIST = sorted(TEMPERATURE_LIST,key = lambda x:int(x['min_C']))#x['min_C']时str类型的,需要转成int比较
    # print(TEMPERATURE_LIST)
for var in TEMPERATURE_LIST[0:50]:
    TOP20_TEM_LIST.append(var['city'])
    TOP20_MIN_LIST.append(var['min_C'])

bar = Bar(r'全国最低温度排名','123456')#制定画布
bar.add(r'地区',TOP20_TEM_LIST,TOP20_MIN_LIST)
bar.show_config()
bar.render(r"从文件中获得的最低温度排名.html")