# -*- coding: utf-8 -*-
import scrapy
from indeed.items import IndeedItem
from bs4 import BeautifulSoup as bs


class IndeedBaseSpider(scrapy.Spider):
    name = "indeed_base"
    # allowed_domains = ["indeed.com"]
    start_urls = (
        'http://www.indeed.com/q-data-scientist-l-San-Francisco,-CA-jobs.html',
    )

    def parse(self, response):
        titles = response.xpath('//h2/a/@title').extract()
        links = response.xpath('//h2/a/@href').extract()
        companies = response.xpath('//span[@class="company"]/span').extract()

        for title, link, comp in zip(titles, links, companies):
            item = IndeedItem()
            item['title'] = title
            abs_url = response.urljoin(link)
            item['url'] = abs_url
            item['company'] = bs(comp).get_text().strip()
            request = scrapy.Request(abs_url, callback=self.parse_job)
            request.meta['item'] = item
            yield request

        # process the next page
        next_page_url = response.xpath(
            '//a[contains(@href, "&pp")]/@href').extract_first()
        abs_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(abs_next_page_url)

    def parse_job(self, response):
        
        item = response.meta['item']
        keys = ['sql', 'python', 'matlab', 'r', 'ml', 'spark', 'hadoop', 'dl', 'mapreduce', 'tf', 'd3', 'sv', 'nn', 'nlp', 'sas']
        skills = ['SQL', 'Python', 'matlab', 'R', 'machine learning', 'Spark', 'Hadoop',
        'deep learning', 'mapreduce', 'tensorflow', 'd3', 'support vector', 'neural network', 'nlp', 'SAS']


        jd = response.text.lower().split(' ')
        for key, skill in zip(keys, skills):
            item[key] = int(skill.lower() in jd)

        yield item
