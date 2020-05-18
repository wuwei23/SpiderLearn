# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exceptions import DropItem

class CnblogspiderPipeline(object):
    def __init__(self):
        self.file = open('paser.json','wb')
    def process_item(self, item, spider):
        if item['title']:
            line = json.dump(dict(item)) + "\n"
            self.file.write(line)
            return item
        else:
            raise DropItem("Missing title in %s" % item)
