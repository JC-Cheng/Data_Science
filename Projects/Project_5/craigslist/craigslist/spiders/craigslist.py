# -*- coding: utf-8 -*-
import scrapy
from re import findall

class CL_Spider(scrapy.Spider):
    name = 'CL'

    def start_requests(self):
        
        urls = [
        'http://newyork.craigslist.org',
        'http://losangeles.craigslist.org',
        'http://chicago.craigslist.org',
        'http://houston.craigslist.org',
        'http://philadelphia.craigslist.org',
        'http://phoenix.craigslist.org',
        'http://sanantonio.craigslist.org',
        'http://sandiego.craigslist.org',
        'http://dallas.craigslist.org',
        'http://sfbay.craigslist.org',
        'http://austin.craigslist.org',
        'http://jacksonville.craigslist.org',
        'http://indianapolis.craigslist.org',
        'http://columbus.craigslist.org',
        'http://charlotte.craigslist.org',
        'http://seattle.craigslist.org',
        'http://denver.craigslist.org',
        'http://elpaso.craigslist.org',
        'http://detroit.craigslist.org',
        'http://washingtondc.craigslist.org',
        'http://boston.craigslist.org',
        'http://memphis.craigslist.org',
        'http://nashville.craigslist.org',
        'http://portland.craigslist.org',
        'http://oklahomacity.craigslist.org',
        'http://lasvegas.craigslist.org',
        'http://baltimore.craigslist.org',
        'http://louisville.craigslist.org',
        'http://milwaukee.craigslist.org',
        'http://albuquerque.craigslist.org',
        'http://tucson.craigslist.org',
        'http://fresno.craigslist.org',
        'http://sacramento.craigslist.org',
        'http://kansascity.craigslist.org',
        'http://atlanta.craigslist.org',
        'http://cosprings.craigslist.org',
        'http://norfolk.craigslist.org',
        'http://raleigh.craigslist.org',
        'http://omaha.craigslist.org',
        'http://miami.craigslist.org',
        'http://minneapolis.craigslist.org',
        'http://tulsa.craigslist.org',
        'http://wichita.craigslist.org',
        'http://neworleans.craigslist.org'
        ]

        # input keyword when activating the spider
        keyword = getattr(self, 'keyword', None)

        if urls is not None and keyword is not None:
            for city_url in urls:
                full_url = city_url + '/search/sss?sort=rel&query=' + keyword
                yield scrapy.Request(full_url, self.parse_CL)

    def parse_CL(self, response):
        
        link = response.url
        dom = findall("(?<=//)\w+",link)[0]
    
        for px in response.xpath('//a[@class="i gallery"]/span[@class="price"]/text()').extract():
            yield {
            'domain': dom,
            'price': px,
            }
        
        # <a href="/search/sss?s=100&amp;query=rv&amp;sort=rel" class="button next" title="next page">
        next_page = response.xpath('//a[@class="button next"]/@href').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, self.parse_CL)