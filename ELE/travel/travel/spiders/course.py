# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 21:11:58 2023

@author: Gowthami
"""

import scrapy

class Quotes(scrapy.Spider):
    name="travel"
    #start_urls=["https://www.amazon.in/s?k=sony+headphone&crid=H6NAQRKJLAPY&sprefix=sony+headphone%2Caps%2C255&ref=nb_sb_noss_2"]
    start_urls=["https://www.tripadvisor.in/Restaurants"]
    def parse(self,response):
        #quotes=response.css ('div.sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16')
        hotels=response.css('.is-6-mobile')
        print(hotels)
        #title=quotes.css('span.a-size-medium a-color-base a-text-normal::text').extract()
        name=hotels.css('.ui_link::text').extract()
        price=hotels.css('._30jeq3::text').extract()
        print(name)
        emi=headphone.css('._18hQoS::text').extract()
        print(price)
        print(emi)
        #author=quotes.css('span.a-offscreen::text').extract()
        for i in range(len(name)):
            yield{"name":name[i],"price":price[i],"emi":emi[i]}