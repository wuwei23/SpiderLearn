#coding:utf-8
#search会扫描整个你string查找匹配
import re
#将正则表达式编译成pattern对象
pattern = re.compile(r'\d+')
result1 = re.search(pattern,'abc192edf')
if result1:
    print(result1.group())#通过group获取捕获的值
else:
    print('匹配失败1')
