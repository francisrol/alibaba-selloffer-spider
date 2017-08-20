#!/usr/bin/env python
# encoding=utf-8

'''
@author: Francis

@license: (C) Copyright 2017
@contact: ryomawithlst@sina.com
@software: PyCharm
@file: config.py
@time: 17/8/18 13:56
@desc:
'''

import pymysql

# MYSQL配置文件
MYSQLCONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "db": "alibaba",
    "user": "alibaba",
    "password": "alibaba",
    "charset": "utf8",
    "cursorclass": pymysql.cursors.DictCursor,
}

# 限制一次允许运行的爬虫数
MAX_SPIDER_NUM = 1

OFFSET = 100    # 单页默认显示条数