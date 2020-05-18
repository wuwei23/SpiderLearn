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

#在写CSS时，标记名不加任何修饰，类名前加“.”，id名前加“#”，使用soup.select()筛选元素，返回类型list

#1通过标记名进行查找
#直接查找title标记
print(soup.select("title"))
#追曾查找title标记
print(soup.select("html head title"))
#直接草诏子节点
#查找head下的title标记
print(soup.select("head > title"))
#查找p下的id="1ink1"的标记
print(soup.select("p > #1ink1"))
#朝朝兄弟节点
#查找id="1ink1"之后，class=sister的所有兄弟标记
print(soup.select("#1ink1 ~ .sister"))
#查找紧跟着id="1ink1"之后，class=sister的子标记
print(soup.select("#1ink1 + .sister"))


#通过CSS的类名查找
print("\n\n\n")
print(soup.select(".sister"))
print(soup.select("[class~=sister]"))


#通过tag的id查找
print("\n\n\n")
print(soup.select("#1ink1"))
print(soup.select("a#1ink2"))


#通过是否存在某个属性来查找
print("\n\n\n")
print(soup.select('a[href]'))


#通过属性值来查找
print("\n\n\n")
print(soup.select('a[href="http://example.com/elsie"]'))
print(soup.select('a[href^="http://example.com/"]'))
print(soup.select('a[href$="tillie"]'))
print(soup.select('a[href*=".com/el"]'))
