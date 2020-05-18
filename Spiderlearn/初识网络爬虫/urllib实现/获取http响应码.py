import urllib.request
try:
    response = urllib.request.urlopen('http://www.zhihu.com')
    print(response)
except urllib.request.HTTPError as e:
    if hasattr(e,'code'):
        print('Error code:',e.code)
