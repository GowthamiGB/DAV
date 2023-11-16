# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 13:55:37 2023

@author: Gowthami
"""
import scrapy

class Quotes(scrapy.Spider):
    name="pdv"
    start_urls=[""]
    def parse(self,response):
        quotes=response.css('div.quote')
        title=quotes.css('span.text::text').extract()
        author=quotes.css('.author::text').extract()
        for i in range(len(title)):
            yield{"title":title[i],"author":author[i]}