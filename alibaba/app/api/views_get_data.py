#!/usr/bin/env python
# encoding=utf-8

'''
@author: Francis

@license: (C) Copyright 2017
@contact: ryomawithlst@sina.com
@software: PyCharm
@file: views_get_data.py
@time: 17/8/15 00:58
@desc:
'''
import json
from datetime import datetime

from flask import make_response, request

from app.api import api
from db import MysqlHandler
from config import OFFSET
db = MysqlHandler()

@api.route("/api/categories/", methods=["GET", "POST"])
def get_categories():
    '''主分类列表信息'''
    categories = db.fetchAll("category")
    return make_response(json.dumps(categories), 200)

@api.route("/api/sub_categories/")
def get_sub_categories():
    '''子分类列表信息'''
    sub_categories = db.fetchAll("sub_category")
    return make_response(json.dumps(sub_categories), 200)

@api.route("/api/category/<shortcut>/")
def get_category(shortcut):
    '''某主分类信息'''
    categories = db.fetchOne("category", where=" where shortcut='%s'"%shortcut)
    return make_response(json.dumps(categories), 200)

@api.route("/api/sub_category/<shortcut>/")
def get_sub_category(shortcut):
    '''某子分类信息'''
    sub_category = db.fetchOne("sub_category", where=" where shortcut='%s'"%shortcut)
    return make_response(json.dumps(sub_category), 200)

@api.route("/api/selloffers/")
def get_selloffers():
    '''获取商家信息列表'''
    cid = request.args['cid']    # 总分类id
    sid = request.args['sid']    # 子分类id
    page = int(request.args["page"])    # 页码
    # 商家总数
    count = db.fetchOne("selloffer", columns=["count(id) as count"], where=" where category_id=%s and sub_category_id=%s"%(cid, sid))["count"]
    # 页面总数
    page_count = float(count)//100 + 1
    # 判断页码
    page = page if page >0 else 1
    # 查询商家信息
    selloffer_list = db.fetchAll("selloffer", where=" where category_id=%s and sub_category_id=%s LIMIT %d,%d"%(cid, sid, (page-1)*100, OFFSET))
    # 查询分类信息
    category = db.fetchOne("category", where=" where id=%s"%cid)
    sub_category = db.fetchOne("sub_category", where=" where id=%s" %sid)
    # 格式化datetime对象
    dtSer = lambda dt: dt.strftime("%Y-%m-%d %H:%M") if dt.year != datetime.now().year else dt.strftime("%m-%d %H:%M")
    result = []
    for s in selloffer_list:
        s['create_time'] = dtSer(s['create_time'])
        result.append(s)
    return make_response(json.dumps(
        {
            "page":page,
            "page_count":page_count,
            "count": count,
            "result":result,
            "category":category,
            "sub_category": sub_category
        }
    ))



