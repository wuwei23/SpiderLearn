import re

#re.sub(pattern,repl,string[,count])
#使用repl替换string中每一个匹配你的字串后返回替换后的字符串
#当repl是一个字符串时，可以使用\id或\g<id>引用分组，但不能使用编号0
#当repl是一个方法时，这个方法应当只接受一个参数，并返回一个字符串用于替换
#count用于指定最多替换次数，不指定时全部替换

p = re.compile(r'(?P<word1>\w+) (?P<word2>\w+)')#使用名称引用
s = 'i say, hello world!'
print(p.sub(r'\g<word2> \g<word1>',s))
p = re.compile(r'(\w+) (\w+)')
print(p.sub(r'\2 \1',s))
def func(m):
    return m.group(2).title() + ' ' + m.group(1).title()
print(p.sub(func,s))
