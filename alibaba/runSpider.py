#!/usr/bin/env python
# encoding=utf-8

'''
@author: Francis

@license: (C) Copyright 2017
@contact: ryomawithlst@sina.com
@software: PyCharm
@file: runSpider.py
@time: 17/8/14 12:15
@desc:
'''
from multiprocessing import Process

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from db import MysqlHandler
db = MysqlHandler()
settings = get_project_settings()


class RunCategorySpider(Process):
    '''启动爬取分类爬虫'''
    def run(self):
        process = CrawlerProcess(settings)
        process.crawl('category')
        process.start()


class RunSellofferSpider(Process):
    '''启动爬取商家信息爬虫'''
    def __init__(self, category_id, sub_category_id):
        super(RunSellofferSpider, self).__init__()
        self.sub_category_id = sub_category_id
        self.category_id = category_id
        self.sub_category = db.fetchOne("sub_category", where=" where id=%s" % self.sub_category_id)
        self.category = db.fetchOne("category", where=" where id=%s" % self.category_id)


    def run(self):

        settings.set("SPIDER_PARAMS", {"CATEGORY": self.category, "SUB_CATEGORY": self.sub_category})
        process = CrawlerProcess(settings)
        process.crawl('selloffer')
        process.start()

    def __str__(self):
        return self.name