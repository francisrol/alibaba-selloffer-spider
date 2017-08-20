#!/usr/bin/env python
# encoding=utf-8

'''
@author: Francis

@license: (C) Copyright 2017
@contact: ryomawithlst@sina.com
@software: PyCharm
@file: manage.py
@time: 17/8/14 16:11
@desc:
'''

from app import create_app
app = create_app()
app.run(debug=True)



