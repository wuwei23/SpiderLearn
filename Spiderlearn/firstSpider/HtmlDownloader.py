#coding:utf-8
import requests
class HtmlDownloader(object):

    def download(self,url):
        if url is None:
            return None
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0'
        headers = {'User-Agent': user_agent}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            r.encoding = 'utf-8'  # 修改编码方式
            return r.text
        return None