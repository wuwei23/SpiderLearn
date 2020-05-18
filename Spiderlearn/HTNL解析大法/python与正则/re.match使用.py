#coding:utf-8
#这个函数是从驶入参数string的开头开始，尝试匹配pattern，一直想后匹配，
#如果遇到无法匹配的字符或者已经匹配到string的末尾，立即返回None
import re
#将正则表达式编译成pattern对象
pattern = re.compile(r'\d+')
#使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
#match是从字符串开头进行匹配，匹配到192立即返回值
result1 = re.match(pattern,'192abc')
if result1:
    print(result1.group())#通过group获取捕获的值
else:
    print('匹配失败1')
result2 = re.match(pattern,'abc192')
if result2:
    print(result2.group())
else:
    print('匹配失败2')