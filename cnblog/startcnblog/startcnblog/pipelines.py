# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import json
import os

#z这边用于写进文本，也可以定义写进数据库中,
class StartcnblogPipeline(object):
    #下面2个函数用于
    def open_spider(self,spider):

        print("开始爬取！！！！")
    def close_spider(self,spider):

        print("爬取结束。。。")


    def process_item(self, item, spider):

        tpl="id:%s\n,title:%s\n,href:%s\n\n"%(item["id"],item["title"],item["href"])
        f=open("text1.json","a",encoding="utf-8")
        f.write(tpl)
        f.close()
        return item

#这边用于在屏幕上输出
class StartcnblogPipeline2(object):


    def process_item(self, item, spider):
        tpl = "id:%s,title:%s,href:%s" % (item["id"], item["title"], item["href"])
        print(tpl)
        return item()