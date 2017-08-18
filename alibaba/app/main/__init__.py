#!/usr/bin/env python
# encoding=utf-8

'''
@author: Francis

@license: (C) Copyright 2017
@contact: ryomawithlst@sina.com
@software: PyCharm
@file: __init__.py
@time: 17/8/14 21:59
@desc:
'''

from flask import Blueprint

main = Blueprint("main", __name__)

from . import views



