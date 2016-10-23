# -*- coding: utf-8 -*-
import scrapy
from indeed.items import IndeedItem
from bs4 import BeautifulSoup as bs

class IndeedBaseSpider(scrapy.Spider):
    name = "indeed_base"
    # allowed_domains = ["indeed.com"]

    def start_requests(self):

        urls = [
        #'http://www.indeed.com/q-data-scientist-l-San-Francisco,-CA-jobs.html', # 2000 San Francisco
        #'http://www.indeed.com/jobs?q=data+scientist&l=New+York%2C+NY',         # 2000 New York
        #'http://www.indeed.com/jobs?q=data+scientist&l=Boston%2C+MA',           # 1600 Boston
        
        #'http://www.indeed.com/jobs?q=data+scientist&l=DC%2C+DC',               # 1500 D.C.
        #'http://www.indeed.com/jobs?q=data+scientist&l=San+Jose%2C+CA',         # 1400 San Jose
        #'http://www.indeed.com/jobs?q=data+scientist&l=Seattle%2C+WA',          # 1200 Seattle
        #'http://www.indeed.com/jobs?q=data+scientist&l=New+Jersey',             # 1000 New Jersey

        #'http://www.indeed.com/jobs?q=data+scientist&l=Texas',                  # 900 Texus
        #'http://www.indeed.com/jobs?q=data+scientist&l=Philadelphia%2C+PA',     # 600 Philadelphia
        #'http://www.indeed.com/jobs?q=data+scientist&l=Los+Angeles%2C+CA',      # 500 Los Angeles
        #'http://www.indeed.com/jobs?q=data+scientist&l=Chicago%2C+IL',          # 500 Chicago

        'http://www.indeed.com/jobs?q=data+scientist&l=Colorado',               # 500 Colorado
        'http://www.indeed.com/jobs?q=data+scientist&l=North+Carolina',         # 500 North Carolina
        'http://www.indeed.com/jobs?q=data+scientist&l=Georgia',                # 500 Georgia
        ]

        for url in urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):

        def find_city(url):
            map = {
            'francisco': 'San Francisco',
            'york': 'New York',
            'boston': 'Boston',
            
            'dc': 'DC',
            'jose': 'San Jose',
            'seattle': 'Seattle',
            'jersey': 'New Jersey',
            
            'texas': 'Texas',
            'phila': 'Philadelphia',
            'angeles': 'Los Angeles',
            'chicago': 'Chicago',
            
            'colorado': 'Colorado',
            'carolina': 'North Carolina',
            'georgia': 'Georgia',
            }

            for key in map:
                if key in url.lower():
                    return map[key]
        
        loc = find_city(response.url)
        titles = response.xpath('//h2/a/@title').extract()
        links = response.xpath('//h2/a/@href').extract()
        companies = response.xpath('//span[@class="company"]/span').extract()

        for title, link, comp in zip(titles, links, companies):
            
            item = IndeedItem()
            item['loc'] = loc
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
        
        keys = ['sql', 'nosql', 'mysql', 'psql', 'mdb', 'pig', 'mahout', 'xls', 'rm',
        'c', 'cpp', 'java', 'js', 'scala', 'ruby', 'python', 'matlab', 'r', 'sas', 'spss',
        'tf', 'torch', 'theano', 'caffe', 'knm',
        'spark', 'hadoop', 'mapreduce', 'mlb', 'hv',
        'd3', 'tab', 'spf', 'nlp', 'pca', 'svm',
        'linux', 'unix', 'gnu', 'git',
        'bs', 'ms', 'phd', 'ctz']
        
        skills = ['sql', 'nosql', 'mysql', 'postgresql', 'mongodb', 'pig', 'mahout', 'excel', 'rapidminer',
        'c', 'c++', 'java', 'javascript', 'scala', 'ruby', 'python', 'matlab', 'r', 'sas', 'spss',
        'tensorflow', 'torch', 'theano', 'caffe', 'knime',
        'spark', 'hadoop','mapreduce', 'mllib', 'hive',
        'd3', 'tableau', 'spotfire', 'nlp', 'pca', 'svm',
        'linux', 'unix', 'gnu', 'git',
        'bs', 'ms', 'phd', 'citizen']

        s_keys = ['ml', 'dl', 'rl', 'sl', 'ul',
        'sml', 'nn', 'ai', 'dm',
        'abt', 'pp', 'dv', 'cv',
        'dt', 'rs',
        'nlp', 'pca', 'svm']
        
        s_skills = ['machine learning', 'deep learning', 'reinforcement learning', 'supervised learning', 'unsupervised learning',
        'semisupervised learning', 'neural network', 'artificial intelligence', 'data mining',
        'ab testing', 'parallel programming', 'data visualization', 'computer vision',
        'decision tree', 'recommendation system',
        'natural language', 'principal component', 'support vector']

        # parse job description
        jd = bs(response.text, 'html.parser').get_text().strip().lower().replace('/', ' ')

        # restore some common strings to desired format
        jd = jd.replace('a b', 'ab')
        jd = jd.replace('c/c++', 'c c++')
        jd = jd.replace("master's", 'master')

        for char in '.-,:;?!':
            jd = jd.replace(char,'')
        
        jd = jd.split(' ')
        jd_len = len(jd)

        # get keywords from jd
        # single keyword
        for key, skill in zip(keys, skills):
            item[key] = int(skill in jd)

        # double keywords
        for key, skill in zip(s_keys, s_skills):
            s = skill.split(' ')
            item[key] = 0

            for i in range(jd_len - 1):
                if s[0] == jd[i] and s[1] == jd[i + 1]:
                    item[key] = 1
                    break
        
        # double check for purls and abbreviations
        for i in range(jd_len - 1):
                if jd[i] == 'decision' and jd[i + 1] == 'trees':
                    item['dt'] = 1
                if jd[i] == 'recommendation' and jd[i + 1] == 'systems':
                    item['rs'] = 1

        # double check for keywords with alias
        if item['d3'] == 0:
            item['d3'] = int('d3js' in jd)        
        if item['bs'] == 0:
            item['bs'] = int('bachelor' in jd)
        if item['ms'] == 0:
            item['ms'] = int('master' in jd)
        if item['ctz'] == 0:
            item['ctz'] = int('citizenship' in jd)
        
        if item['nlp'] == 0:
            item['nlp'] = int('nlp' in jd)
        if item['pca'] == 0:
            item['pca'] = int('pca' in jd)
        if item['svm'] == 0:
            item['svm'] = int('svm' in jd)

        yield item