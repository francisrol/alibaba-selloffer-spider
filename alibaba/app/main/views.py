#!/usr/bin/env python
# encoding=utf-8

'''
@author: Francis

@license: (C) Copyright 2017
@contact: ryomawithlst@sina.com
@software: PyCharm
@file: views_get_data.py
@time: 17/8/14 22:00
@desc:
'''

from flask import render_template

from app.main import main
from db import MysqlHandler
db = MysqlHandler()

@main.route("/")
def index():
    categories = db.fetchAll("category")
    result = []
    for category in categories:
        sub_categories = db.fetchAll("sub_category", where=" where parent='%s'"%category["name"])
        category["sub_categories"] = sub_categories
        result.append(category)
    return render_template("index.html", categories=result)


