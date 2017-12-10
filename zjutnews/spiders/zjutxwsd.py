# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import ZjutItem
from  scrapy.selector  import  Selector


class JhSpider(scrapy.Spider):
    name = 'zjutxwsd'
    allowed_domains = ['zjut.edu.cn']
    start_urls = ['http://www.zjut.edu.cn/BigClass.jsp?bigclassid=10']

    def parse_detail(self, response):
        sel = Selector(response)
        item = ZjutItem()
        inf = sel.xpath("//div[@align='center']").extract()[4]
        inf = re.sub(r'<.*?>',"",inf)
        inf = inf.split("：")
        fonts = sel.xpath("//div [@id='jiacu']/font")
        content = ""
        for p in fonts.xpath(".//p"):
            content = content + p.extract().strip()
            content = re.sub(r'<p.*?>',"",content)
            content = re.sub(r'</p>',"\r",content)
            content = re.sub(r'<br>', "\r", content)
            content = re.sub(r'<.*?>', "", content)
            content = re.sub(r'<img.*?>', "", content)
            item['content'] = content
        item['title'] = sel.xpath("//div [@align='center'][@class='newstitle']/text()").extract()[0]
        item['date'] = inf[2].strip(u"点击率").strip()
        item['author'] = inf[1].lstrip().rstrip(u"日\xa0\xa0期").strip()
        item['category'] = 10
        if sel.xpath("//*[@id='jiacu']/font/p/img/@src").extract() == []:
            item['image'] = ""
        else:
            item['image'] = 'http://www.zjut.edu.cn/' + sel.xpath("//*[@id='jiacu']/font/p/img/@src").extract()[0]


        yield item

    def parse(self, response):
        sel = Selector(response)
        url_s = response.url.split("/")
        sel = Selector(response)
        item = ZjutItem()
        sites = sel.xpath("//span[@class='news']")
        sites.reverse()
        for site in sites:
            link = site.xpath("a/@href").extract()[0]
            url_detail = 'http://www.zjut.edu.cn/%s' % (link)
            yield scrapy.Request(url_detail, callback=self.parse_detail)
        s1 = u'下一页'
        url = 'http://www.zjut.edu.cn/' + sel.xpath("//a[text()='[%s]']/@href" % (s1)).extract()[0]
        item['url'] = url
        yield scrapy.Request(url, callback=self.parse)


