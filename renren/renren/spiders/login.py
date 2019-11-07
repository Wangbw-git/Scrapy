# -*- coding: utf-8 -*-
import scrapy


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/SysHome.do']

    def parse(self, response):
        formdata = {
            "email":"Wangbw111@163.com",
            "password":"pythonapider",
        }
        yield scrapy.FormRequest.from_response(response,formid="loginForm",formdata=formdata,callback=self.after_login)

    def after_login(self,response):
        with open('renren.html','w',encoding='utf-8') as fp:
            fp.write(response.text)
