from bs4 import BeautifulSoup
import bs4
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
<p class="story">...</p
"""

soup = BeautifulSoup(html_str,'lxml')

#所有对象可以归纳为四种

#1、Tag通俗说就是标记如<title>The Dormouse's story</title>里的title标记及其里面的内容
#抽取title
print(soup.title)
#使用这种方式比使用正则简单，但查找的内容是所有内容中第一个符合要求的标记
#Tag有两个属性，name和attributes
print(soup.name)#soup对象本身的名字为[document]
print(soup.title.name)
#Tag不仅可以获取name，还可以修改name，改变之后将影响所有通过当前BeautifulSoup
# 对象生成的HTML文档
soup.title.name = 'mytitle'
print(soup.title)#修改后其值变为None
print(soup.mytitle)
#<p class="title"><b>The Dormouse's story</b></p>中有一个class属性，值为title
#其操作方法与字典相同
print(soup.p['class'])
print(soup.p.get('class'))
#也可以直接.取属性，比如.attrs获取Tag中所有属性
print(soup.p.attrs)
#和name一样，可以对标记中的属性和内容进行修改
soup.p['class'] = "myClass"
print(soup.p)


#NavigableString
#我们已经得到了标记的内容，想要获得标记的内部的文字要用到.string
print(soup.p.string)
print(type(soup.p.string))
#一个NavigableString字符串和python中的Unicode字符串相同，通过unicode()方法可以转换
unicode_string = ''.join(soup.p.string)#先转成str类型
print(type(unicode_string))
print(unicode_string)
unicode_string = unicode_string.encode()
print(type(unicode_string))



#BeautifulSoup
#BeautifulSoup对象表示的是一个文档的全部内容。大部分时候，可以把他当作Tag对象，是一个特殊的
#Tag，因为Beautifulsoup对象并不是真正的HTML或XML标记，所以他没有name和attr属性，但为了
#将BeautifulSoup对象标准化为Tag对象，实现接口的统一，仍然可以分别获取他的name和attr属性
print(type(soup.name))#类型是str
print(soup.name)
print(soup.attrs)



#Comment
#以上三种覆盖后剩下的一些特殊的内容，比如文档的注释部分
print(soup.a.string)
print(type(soup.a.string))
#当使用.string输出他的内容时，会发现已经将注释符号去掉了，输出他的内省会发现时Comment
#如果在不清楚这个标记.string的情况下，可能会造成数据混乱，因此提取字符串时，可以判断类型
if type(soup.a.string) == bs4.element.Comment:
    print(type(soup.a.string))