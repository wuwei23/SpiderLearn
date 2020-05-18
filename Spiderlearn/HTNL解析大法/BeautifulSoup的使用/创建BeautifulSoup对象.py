from bs4 import BeautifulSoup

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

#通过字符串创建
soup = BeautifulSoup(html_str,'lxml',from_encoding='utf-8')
#通过文件来创建
#soup = BeautifulSoup(open('index.html'))
#输出
print(soup.prettify())