# -*- coding: utf-8 -*-
import scrapy,re
from csdn.items import CsdnItem

class CsdnSpiderSpider(scrapy.Spider):
    name = 'csdn_spider'
    allowed_domains = ['edu.csdn.net']
    start_urls = ['https://edu.csdn.net/courses/k/p1']

    def parse(self, response):
        details_url = response.xpath("//div[@class='course_item']/a/@href").extract()
        for url in details_url:
            # print(url)
            fullurl = "".join(url)
            yield scrapy.Request(url=fullurl,callback=self.parse_detail)

    def parse_detail(self,response):
        item = CsdnItem()
        item['title'] = response.xpath("//div[contains(@class,'info_right')]/h1/text()").extract_first()
        number = response.xpath("//div[@class='course_status']/span/text()").extract_first()
        item['number'] = number.replace("人已学习","")
        price = response.xpath("//div[@class='price_wrap']/span[@class='money']/text()").extract_first()
        item['price'] = price.replace("¥","")
        item['teacher'] = response.xpath("//div[@class='professor_name']/a/text()").extract_first()
        item['cover'] = response.xpath("//div[contains(@class,'info_left')]/a/img/@src").extract_first()
        intros = response.xpath("//div[contains(@class,'outlin_discribe')]//text()").extract()
        intro = "".join(intros)
        item['intro'] = re.sub(r'\s','',intro)
        # item['sections'] = response.xpath("//span[@class='ellipsis']/text()").extract()
        sections = response.css("dt.clearfix span::text,span.ellipsis::text").getall()
        item['sections'] = "".join(sections)
        # print(item)
        yield item