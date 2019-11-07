# -*- coding: utf-8 -*-
import scrapy


class SinaSpiderSpider(scrapy.Spider):
    name = 'sina_spider'
    allowed_domains = ['news.sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        chapters = []
        sections = response.xpath("//div[@class='section']")
        for section in sections:
            navs = section.xpath("./div")
            for nav in navs:
                mainCategory = nav.xpath("./h3/a/text()").get()
                categories = nav.xpath("./ul/li/a/text()").getall()
                chapters.append({
                    'main':mainCategory,
                    'categories':categories,
                })

        print(chapters)
