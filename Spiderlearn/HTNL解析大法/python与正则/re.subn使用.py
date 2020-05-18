import re
#subn会多返回一个替换次数
s = 'i say, hello world!'
p = re.compile(r'(\w+) (\w+)')
print(p.subn(r'\2 \1',s))
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
print(p.subn(func,s))
