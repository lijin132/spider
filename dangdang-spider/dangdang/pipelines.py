# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangPipeline(object):
    def process_item(self, item, spider):
        # item=dict(item)
        # print(len(item("name")))
        for j in range(0, len(item["title"])):
            print(j)
            name=item["title"][j]
            num=item["num"][j]
            print("商品名："+name)
            print("商品评论数："+num)
            print("--------------------------")
        return item
