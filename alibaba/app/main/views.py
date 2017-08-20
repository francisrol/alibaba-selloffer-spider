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
import os

from flask import render_template, g, request, session, redirect

from app.main import main
from db import MysqlHandler
from app.decorators import is_login
db = MysqlHandler()


@main.route("/")
@is_login
def index():
    # 查询出所有分类信息
    categories = db.fetchAll("category")
    result = []
    for category in categories:
        # 找出所有子分类信息
        sub_categories = db.fetchAll("sub_category", where=" where parent='%s'"%category["name"])
        category["sub_categories"] = sub_categories
        result.append(category)
    # 首页显示的数据信息
    first_cid = categories[0]["id"]
    first_sid = categories[0]["sub_categories"][0]["id"]
    # 返回
    return render_template("index.html", categories=result, first_cid=first_cid, first_sid=first_sid)

@main.route("/login/", methods=["GET",'POST'])
def login():
    '''管理员登录'''
    message = ''
    # 从系统环境变量获取
    USERNAME = os.environ.get("ALIBABA_SELLOFFER_USERNAME", 'admin')
    PASSWORD = os.environ.get("ALIBABA_SELLOFFER_PASSWORD", 'itcast')
    # 从表单提取数据
    username = request.form.get("username")
    password = request.form.get("password")
    # 验证登录
    if username == USERNAME and password == PASSWORD:
        # 设置session
        session["username"] = username
        return redirect('/')
    # 如果是从当前页跳转的，这两个值会相等
    if request.referrer == request.url:
        message = u"用户名或密码错误！"
    return render_template("sign_in.html", message=message)

