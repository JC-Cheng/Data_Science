# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IndeedItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # basic info
    title = scrapy.Field()
    url = scrapy.Field()
    company = scrapy.Field()

    # skills
    sql = scrapy.Field()
    python = scrapy.Field()
    matlab = scrapy.Field()
    r = scrapy.Field()
    ml = scrapy.Field()

    spark = scrapy.Field()
    hadoop = scrapy.Field()
    dl = scrapy.Field()
    mapreduce = scrapy.Field()
    tf = scrapy.Field()
    
    d3 = scrapy.Field()
    sv = scrapy.Field()
    nn = scrapy.Field()
    nlp = scrapy.Field()
    sas = scrapy.Field()
