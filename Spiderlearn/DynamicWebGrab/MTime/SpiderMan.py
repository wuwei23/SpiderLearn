from py文件.Spiderlearn.DynamicWebGrab.MTime.HtmlParser import HtmlParser
from py文件.Spiderlearn.DynamicWebGrab.MTime.HtmlDownloader import HtmlDownloader
import time

class SpiderMain(object):
    def __init__(self):
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()

    def crawl(self, root_url):
        content = self.downloader.download(root_url)
        #print(content)
        urls = self.parser.parser_url(root_url, content)
        #print(urls)

        #构造一个活的评分和票房链接
        for url in urls:
            try:
                t = time.strftime("%Y%m%d%H%M%S3282", time.localtime())
                rank_url = 'http://service.library.mtime.com/Movie.api' \
                           '?Ajax_CallBack=true' \
                           '&Ajax_CallBackType=Mtime.Library.Services' \
                           '&Ajax_CallBackMethod=GetMovieOverviewRating' \
                           '&Ajax_CrossDomain=1' \
                           '&Ajax_RequestUrl=%s' \
                           '&t=%s' \
                           '&Ajax_CallBackArgument0=%s' %(url[0],t,url[1])
                #print(rank_url)
                rank_content = self.downloader.download(rank_url)
                data = self.parser.parser_json(rank_url, rank_content)
                #print(data)
                with open("data.txt",'a',encoding='utf-8') as fp:
                    fp.write(str(data)+"\n")
            except Exception as e:
                print("Crawl failed")

if __name__ == '__main__':
    spier = SpiderMain()
    spier.crawl('http://theater.mtime.com/China_Jiangsu_Province_Nanjing/')