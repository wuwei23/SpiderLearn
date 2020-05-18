from bs4 import BeautifulSoup

html_str  = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class=story>Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="1ink1"><!--Elsie--></a>,
<a href="http://example.com/lacie" class="sister" id="1ink2"><!--lacie--></a>and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p
"""

soup = BeautifulSoup(html_str,'lxml')

#BeautifulSoup会将HTML转化为文档树进行搜索，树形结构的节点概念

#子节点
#Tag中的.content属性可以将Tag子节点以列表的方式输出
print('1')
print(soup.head.contents)
#获取列表的大小
print('2')
print(len(soup.head.contents))
print(soup.head.contents[0].string)
#若字符串中没有.contents属性，因为字符串没有子节点
#。children属性返回一个生成器，可以对Tag节点进行循环
print('3')
for child in soup.head.children:
    print(child)
#.descendants属性可以对所有Tag的子孙节点进行递归循环,包含title属性及其里面的内容
print('4')
for child in soup.head.descendants:
    print(child)
#获取子节点的内容
#.string一个标记里面没有标记或只有唯一一个标记，返回最里面的内容，标记很多则返回None
print('5')
print(soup.head.string)
print(soup.title.string)
print(soup.html.string)
#.strings属性用于Tag中包含对各字符串的情况，可以进行循环遍历
print('6')
for string in soup.strings:
    print(repr(string))
#.stripped_strings属性可以去掉输出字符串中包含的空格或空行
print('7')
for string in soup.stripped_strings:
    print(repr(string))


#父节点
#通过.parent属性来获取某个元素的父节点
print('\n\n\n')
print('1')
print(soup.title)
print(soup.title.parent)
#.parents属性可以递归得到所有的父辈节点
print('2')
print(soup.a)
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)


#兄弟节点
#.next_sibling属性可以获取该节点的下一个兄弟节点， .previous_sibling则与之相反
#如果节点不存在，则返回None
print('\n\n\n')
print('1')
print(soup.p.next_sibling)
print(soup.p.prev_sibling)
print(soup.p.next_sibling.next_sibling)
#第一个输出结果为空白，因为空白也被视为一个节点
#通过.next_siblings和.previous_siblings属性可以对当前节点的兄弟节点迭代输出
print('2')
for sibling in soup.a.next_siblings:
    print(repr(sibling))


#前后节点
#使用.next_element与.previous_element这两个属性，针对所有节点，不分层次
print('\n\n\n')
print('1')
print(soup.head)
print(soup.head.next_element)
#通过.next_elements与.previous_elements的迭代器可以遍历所有的前节点或后节点
print('2')
for element in soup.a.next_elements:
    print(repr(element))