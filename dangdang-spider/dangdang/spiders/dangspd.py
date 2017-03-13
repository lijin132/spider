# -*- coding: utf-8 -*-
import scrapy
import re
from dangdang.items import DangdangItem
from scrapy.http import Request


class DangspdSpider(scrapy.Spider):
    name = "dangspd"
    allowed_domains = ["dangdang.com"]
    start_urls = [
        'http://search.dangdang.com/?key=python&act=input&d \
            dt-rpm=undefined&page_index=1']

    def parse(self, response):
        item = DangdangItem()
        item["title"] = response.xpath(
            "//a[@class='pic']/@title").extract()  # 分析网页结构，使用xpath
        item["num"] = response.xpath(
            "//a[@class='search_comment_num']/text()").extract()
        yield item
        for i in range(2, 19):
            url = "http://search.dangdang.com/?key=python&act= \
                input&ddt-rpm=undefined&page_index=" + \
                str(i)  # 网址
            yield Request(url, callback=self.parse)  # 回调
