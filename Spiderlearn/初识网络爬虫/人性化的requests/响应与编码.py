import requests
import chardet  #字符串/文件编码检测模块
r = requests.get('http://www.baidu.com')
print('content-->' ,chardet.detect(r.content))
print('content-->' ,r.content)#字节形式
print('text-->' + r.text)#文本形式
print('encoding-->' + r.encoding)#网页编码格式
#r.encoding = 'utf-8'#手动设置编码格式，但略显笨拙
#直接将chardet探测到的编码，赋给r.encoding实现解码，r.text就不会有乱码了
r.encoding = chardet.detect(r.content)['encoding']
print('new text-->' + r.text)


#流模式，设置stream=True标志位，使响应以字节流方式进行读取
# r.raw.read函数指定读取字节数
r = requests.get('http://wwww.baidu.com',stream=True)
print(r.raw.read(10))