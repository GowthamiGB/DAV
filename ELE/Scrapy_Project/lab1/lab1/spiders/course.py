# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 14:57:58 2023

@author: Gowthami
"""

import scrapy
from ..items import Lab1Item
class QuoteSpider(scrapy.Spider):
    name='lab1'
    start_urls=['https://quotes.toscrape.com/']
    
    def parse(self,response):
        #title=response.css('title::text').extract()
        all_div_quotes=response.css('div.quote')
        title=all_div_quotes.css('span.text::text').extract()
        author=all_div_quotes.css('.author::text').extract()
        tag=all_div_quotes.css('.tag::text').extract()
        for i in range(len(title)):
                yield{'title':title[i],'author':author[i],'tag':tag[i]}
    
    """def parse(self, response):
        #1.quotes 2.Author 3.tag
        items=Lab1Item()
        all_div_quotes=response.css('div.quote')
        for quotes in all_div_quotes:
            title=all_div_quotes.css('span.text::text').extract() 
            author=all_div_quotes.css('.author::text').extract() 
            tag=all_div_quotes.css('.tag::text').extract()
            
            items['title']=title
            items['author']=author
            items['tag']=tag
            yield items"""
            
