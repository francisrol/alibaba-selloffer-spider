#!/usr/bin/env python
# encoding=utf-8

'''
@author: Francis

@license: (C) Copyright 2017
@contact: ryomawithlst@sina.com
@software: PyCharm
@file: views_make_action.py
@time: 17/8/15 11:43
@desc:
'''

from flask import make_response, request

from app.api import api
from runSpider import RunSellofferSpider, RunCategorySpider
from config import MAX_SPIDER_NUM

# 存储爬虫
spiders = []

#  过滤已经结束的爬虫
def filter_alive_spider():
    # 过滤已经结束的爬虫：
    for spider in spiders:
        if not spider.is_alive():
            # 如果已经不活跃，那么将其删除
            spiders.remove(spider)

@api.route("/api/spider/start/")
def start_spider():
    '''启动指定爬虫'''
    filter_alive_spider()
    # 判断当前活跃爬虫总数是否达到上限
    if len(spiders) >= MAX_SPIDER_NUM:
        return make_response(u"Fail!当前启动的爬虫已达上限，请关闭其他爬虫，或者等待其他爬虫结束！")

    params = request.args
    category_id = params.get("cid")
    sub_category_id = params.get("sid")

    for spider in spiders:
        # 判断是否重复启动
        if spider.category_id==category_id and  spider.sub_category_id==sub_category_id:
            return make_response(u"Fail!爬虫\"%s\"已经启动"%spider.sub_category["name"])
    # 启动新爬虫
    p = RunSellofferSpider(category_id, sub_category_id)
    spiders.append(p)
    p.start()
    return make_response(u"Success!爬虫\"%s\"启动成功"%p.sub_category["name"])

@api.route("/api/spider/stop/")
def stop_spider():
    '''停止指定爬虫'''
    params = request.args
    category_id = params.get("cid")
    sub_category_id = params.get("sid")
    for spider in spiders:
        # 如果存在指定的爬虫，那么将其终结掉，并从管理中删除
        if spider.category_id == category_id and spider.sub_category_id==sub_category_id:
            spider.terminate()
            spiders.remove(spider)
            return make_response(u"Success! 爬虫 \"%s\" 已经停止."%spider.sub_category["name"])
    else:
        return make_response(u"Fail!该爬虫未启动，或者已经结束")

@api.route("/api/spider/check/")
def check_running_spider():
    '''查看正在运行的爬虫'''
    filter_alive_spider()
    alive_spider = '\n'.join(["\t"+s.sub_category["name"] for s in spiders])
    data = u"正在运行的爬虫：\n %s \n "%alive_spider if alive_spider else u'未找到正在运行的爬虫'
    return make_response(data)

@api.route("/api/update/categories/")
def update_categories():
    p = RunCategorySpider()
    p.start()
    p.sub_category = {}
    p.sub_category["name"] = u"分类更新爬虫"
    spiders.append(p)
    return make_response("<p>正在更新...<\p>"
                         "<a href='/api/spider/check/'>点击  </a>检查正在运行的爬虫")


