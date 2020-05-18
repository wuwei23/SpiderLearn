#coding:utf-8
# import sys
# import os
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# rootPath = os.path.split(rootPath)[0]
# sys.path.append(os.path.split(rootPath)[0])

import scrapy
from cnblogSpider.cnblogSpider.items import CnblogspiderItem
from scrapy.selector import Selector

class CnblogsSpider(scrapy.Spider):
    name = "cnblogs" #爬虫的名称
    allowed_domains = ["cnblogs.com"] #允许的域名
    start_urls = [
        "https://www.cnblogs.com/qiyeboy/default.html"
    ]

    def parse(self, response):
        #实现网页的解析
        #首先抽取所有的文章
        papers = response.xpath(".//*[@class='day']")
        #从每篇文章中抽取数据
        for paper in papers:
            url = paper.xpath(".//*[@class='postTitle']/a/@href").extract()[0]
            title = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
            time = paper.xpath(".//*[@class='dayTitle']/a/text()").extract()[0]
            content = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
            item = CnblogspiderItem(url=url,title=title,time=time,content=content)
            yield item
        next_page = Selector(response).re(u'<a href="(\S*)">下一页</a>')
        if next_page:
            yield scrapy.Request(url=next_page[0],callback=self.parse)