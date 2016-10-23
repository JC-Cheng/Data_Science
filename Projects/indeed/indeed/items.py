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
    loc = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    company = scrapy.Field()

    # db skills
    sql = scrapy.Field()
    nosql = scrapy.Field()
    mysql = scrapy.Field()
    psql = scrapy.Field()
    mdb = scrapy.Field()
    pig = scrapy.Field()
    mahout = scrapy.Field()
    xls = scrapy.Field()
    rm = scrapy.Field()
    # 'sql', 'nosql', 'mysql', 'psql', 'mdb', 'pig', 'mahout', 'xls', 'rm',

    # program skills
    c = scrapy.Field()
    cpp = scrapy.Field()
    java = scrapy.Field()
    js = scrapy.Field() 
    scala = scrapy.Field()
    ruby = scrapy.Field()
    python = scrapy.Field()
    matlab = scrapy.Field()
    r = scrapy.Field()
    sas = scrapy.Field()
    spss = scrapy.Field()
    # 'c', 'cpp', 'java', 'js', 'scala', 'ruby', 'python', 'matlab', 'r', 'sas', 'spss',
    
    # libar
    tf = scrapy.Field()
    torch = scrapy.Field()
    theano = scrapy.Field()
    caffe = scrapy.Field()
    knm = scrapy.Field()
    # 'tf', 'torch', 'theano', 'caffe', 'knm',

    #
    spark = scrapy.Field()
    hadoop = scrapy.Field()
    mapreduce = scrapy.Field()
    mlb = scrapy.Field()
    hv = scrapy.Field()
    # 'spark', 'hadoop','mapreduce', 'mlib', 'hive', 
    
    # os
    linux = scrapy.Field()
    unix = scrapy.Field()
    gnu = scrapy.Field()
    git = scrapy.Field()
    # 'linux', 'unix', 'gnu', 'git',
    
    # visualizations
    d3 = scrapy.Field()
    tab = scrapy.Field()
    spf = scrapy.Field()
    # 'tab','nlp'
    # 'd3', 'tab', 'spf'

    # buzz words or algos
    ml = scrapy.Field()
    dl = scrapy.Field()
    rl = scrapy.Field()
    sl = scrapy.Field()
    ul = scrapy.Field()
    sml = scrapy.Field()

    nn = scrapy.Field()
    ai = scrapy.Field()
    dm = scrapy.Field()
    abt = scrapy.Field()
    pp = scrapy.Field()
    dv = scrapy.Field()
    cv = scrapy.Field()
    #'ml', 'dl', 'rl', 'sl', 'ul', 'sv', 'nn', 'ai', 'dm', 'abt', 'dt', 'pp'

    dt = scrapy.Field() # tree or trees
    rs = scrapy.Field() # system or systems

    svm = scrapy.Field()
    nlp = scrapy.Field()
    pca = scrapy.Field()
    # 'nlp', 'pca', 'svm'
    
    # education
    bs = scrapy.Field()
    ms = scrapy.Field()
    phd = scrapy.Field()
    ctz = scrapy.Field()
    # 'ba', 'ma', 'phd', 'ctz'