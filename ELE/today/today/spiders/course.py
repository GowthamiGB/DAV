# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 20:34:18 2023

@author: Gowthami
"""

import scrapy

class Quotes(scrapy.Spider):
    name="today"
    #start_urls=["https://www.amazon.in/s?k=sony+headphone&crid=H6NAQRKJLAPY&sprefix=sony+headphone%2Caps%2C255&ref=nb_sb_noss_2"]
    start_urls=["https://www.flipkart.com/clothing-and-accessories/winter-wear/sweatshirt/men-sweatshirt/pr?sid=clo,qvw,64a,vui&otracker=categorytree&otracker=nmenu_sub_Men_0_Sweatshirts"]
    def parse(self,response):
        #quotes=response.css('div.sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16')
        headphone=response.css('._2B099V')
        print(headphone)
        #title=quotes.css('span.a-size-medium a-color-base a-text-normal::text').extract()
        name=headphone.css('._2WkVRV::text').extract()
        price=headphone.css('._30jeq3::text').extract()
        print(name)
        emi=headphone.css('._18hQoS::text').extract()
        print(price)
        print(emi)
        #author=quotes.css('span.a-offscreen::text').extract()
        for i in range(len(name)):
            yield{"name":name[i],"price":price[i],"emi":emi[i]}