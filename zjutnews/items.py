# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class ZjutItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    content = scrapy.Field()#内容
    title = scrapy.Field()# 标题
    url = scrapy.Field()
    date = scrapy.Field()
    image = scrapy.Field()
    author = scrapy.Field()
    category = scrapy.Field()  # 类别 int

    #created = scrapy.Field()#爬取时间

    #created_at = scrapy.Field()#创建时间
    #update_at = scrapy.Field()#更新时间
    #href = scrapy.Field()
