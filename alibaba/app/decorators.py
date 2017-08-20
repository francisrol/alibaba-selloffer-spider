#!/usr/bin/env python
# encoding=utf-8

'''
@author: Francis

@license: (C) Copyright 2017
@contact: ryomawithlst@sina.com
@software: PyCharm
@file: decorators.py
@time: 17/8/20 11:42
@desc:
'''
from functools import wraps
from flask import session, redirect

def is_login(func):
    @wraps(func)
    def inner(*args, **kwargs):
        username = session.get("username")
        if not username:
            return redirect('/login/')
        return func(*args, **kwargs)
    return inner


