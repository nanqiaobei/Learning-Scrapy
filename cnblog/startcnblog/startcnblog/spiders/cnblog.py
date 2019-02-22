# -*- coding: utf-8 -*-
import scrapy
import sys
import io
from scrapy.selector import Selector,HtmlXPathSelector
from scrapy.http import Request
from ..items import StartcnblogItem


class CnblogSpider(scrapy.Spider):
    name = 'cnblog'
    allowed_domains = ['cnblogs.com']
    start_urls = ['https://www.cnblogs.com/']
    visited_url = set()

    def parse(self, response):
        hxs=Selector(response=response).xpath("//div[@id='post_list']")
        for info in hxs:
            title=info.xpath(".//a[@class='titlelnk']/text()").extract()
            href=info.xpath(".//a[@class='titlelnk']/@href").extract()
            id=info.xpath(".//a[@class='lightblue']/text()").extract()
            total_info=StartcnblogItem(title=title,href=href,id=id)
            yield total_info
        hxs1=Selector(response=response).xpath("//div[@id='paging_block']/div[@class='pager']")
        for i in hxs1 :
            b = i.xpath("./a/@href").extract()
            for url in b:
                md5_url=self.md5(url)
                if md5_url in self.visited_url:
                    pass
                else:
                    self.visited_url.add(url)

                    url = "http://www.cnblogs.com/%s" % url
                    print(url)
                    yield Request(url=url, callback=self.parse)


    def md5(self, url):
        import hashlib
        obj = hashlib.md5()
        obj.update(bytes(url, encoding='utf-8'))
        return obj.hexdigest()

