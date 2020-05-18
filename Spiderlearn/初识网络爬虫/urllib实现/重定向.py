#自动重定向
# import urllib.request
# response = urllib.request.urlopen('http://www.zhihu.com/')
# isRedirected = response.geturl() == 'http://www.zhihu.com/'
# print(isRedirected)
# print(response.geturl())

#不想自动重定向
import urllib.request
class RedirectHandler(urllib.request.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        pass
    def http_error_302(self, req, fp, code, msg, headers):
        result = urllib.request.HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, headers)
        result.status = code
        result.newurl = result.geturl()
        return result
opener = urllib.request.build_opener(RedirectHandler)
opener.open('http://www.zhihu.cn')