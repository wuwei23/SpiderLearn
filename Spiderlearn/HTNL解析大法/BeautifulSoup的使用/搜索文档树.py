from bs4 import BeautifulSoup
import re

html_str  = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class=story>Once upon a time there were three little sisters; and their names
were
<a href="http://example.com/elsie" class="sister" id="1ink1"><!--Elsie--></a>,
<a href="http://example.com/lacie" class="sister" id="1ink2"><!--lacie--></a>and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<div data-foo="value">foo!</div>
<p class="story">...</p

"""

soup = BeautifulSoup(html_str,'lxml')

#find_all()方法的函数原型
# find_all(name,attrs,recursive,text,**kwargs)
#name参数
#可以查找所有名为name的标记，字符串会被自动忽略掉。name参数取值可以是字符串，列表，正则表达式和方法
print('1')
print(soup.find_all('b'))#差找文档内的<b>标记
#如果传入正则表达式作为参数，BeautifulSoup会通过正则表达式的match()来匹配内容
print('2')
for tag in soup.find_all(re.compile("^b")):#匹配所有以<b>开头的标记
    print(tag.name)
#如果传入看i额表参数，BeautifulSoup会将列表的任意元素匹配的内容返回
print('3')
print(soup.find_all(["a","b"]))#匹配所有的<a>和<b>标记
#如果传入的参数时True，可以匹配任何值
print('4')
for tag in soup.find_all(True):#查找所有Tag，但不会返回字符串
    print(tag.name)
#如果没有合适的过滤器，还可以定义一个方法，方法只接受一个Tag节点，
# 如果其返回True表示当前元素匹配并且被找到，不是则返回False
print('5')
def hasClass_Id(tag):#找到所有包含class与id属性的元素
    return tag.has_attr('class') and tag.has_attr('id')
print(soup.find_all(hasClass_Id))



#kwargs元素
#如果一个指定的参数不是搜索内置的参数名，搜索时会把该参数当作指定名字Tag的属性来搜索
#搜索指定名字的属性时可以使用的参数包括字符串，正则表达式，列表，True
print('\n\n\n')
print('1')
print(soup.find_all(id='1ink1'))
#传入href参数，BeautifulSoup会搜索每个Tag的href属性
print('2')
print(soup.find_all(href = re.compile("elsie")))
#True查找所有
print('3')
print(soup.find_all(id=True))
#使用class过滤要在class后加下划线
print('4')
print(soup.find_all("a",class_ = "sister"))
#多个指定名字的参数同时过滤
print('5')
print(soup.find_all(href=re.compile("elsie"),id='1ink1'))
#有些tag属性不能用，就比如HTML5中的 data-* 属性
# data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
# data_soup.find_all(data-foo="value")
#报错 SyntaxError: keyword can't be an expression
#可以通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag:
print('6')
print(soup.find_all(attrs={"data-foo": "value"}))


#text参数
#可以搜索文档中的字符串内容
print('\n\n\n')
print(soup.find_all(text="Elsie"))
print(soup.find_all(text=["Tillie","Elsie","Lacie"]))
print(soup.find_all(text=re.compile("Dormouse")))
print(soup.find_all("a",text="Elsie"))


#limit参数
#限制返回的结果的数量
print('\n\n\n')
print(soup.find_all("a",limit=2))


#recursive参数
#调用find_all时，会检索当前tag所有的子孙节点，如果只想检索Tag的子节点，可以使用
print(soup.find_all("title"))
print(soup.find_all("title",recursive=False))