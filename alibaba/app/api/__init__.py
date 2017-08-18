#!/usr/bin/env python
# encoding=utf-8

'''
@author: Francis

@license: (C) Copyright 2017
@contact: ryomawithlst@sina.com
@software: PyCharm
@file: __init__.py
@time: 17/8/15 00:57
@desc:
'''

from flask import Blueprint

api = Blueprint("api", __name__)

from . import views_get_data, views_make_action

