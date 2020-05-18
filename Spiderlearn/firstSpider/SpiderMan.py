#coding:utf-8
from py文件.Spiderlearn.firstSpider.packet.HtmlDownloader import HtmlDownloader
from py文件.Spiderlearn.firstSpider.packet.HtmlParser import HtmlParser
from py文件.Spiderlearn.firstSpider.packet.UrlManager import UrlManager
from py文件.Spiderlearn.firstSpider.packet.DataOutput import DataOutput

class SpiderMan(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self,root_url):
        #添加入口url
        self.manager.add_new_url(root_url)
        #判断url管理器中是否有新的url，同时判断抓取了多少个url
        while (self.manager.has_new_url() and self.manager.old_url_size() < 100):
            try:
                #从url管理器获取新的url
                new_url = self.manager.get_new_url()
                #HTML下载器下载网页
                html = self.downloader.download(new_url)
                # print(html)
                #HTML解析器抽取网页数据
                new_urls,data = self.parser.parser(new_url,html)
                #将抽取的url添加到url管理器中
                self.manager.add_new_urls(new_urls)
                #数据存储器存储文件
                self.output.store_data(data)
                # print(self.output.datas)
                print("已经抓取了%s个链接" % self.manager.old_url_size())
            except Exception as e:
                print("crawl failed")
            #数据存储器将文件输出成指定格式
        self.output.output_html()


if __name__ == "__main__":
    spider_man = SpiderMan()
    spider_man.crawl("https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB")