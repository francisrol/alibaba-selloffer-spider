#!/usr/bin/env python
# encoding=utf-8

'''
@author: Francis

@license: (C) Copyright 2017
@contact: ryomawithlst@sina.com
@software: PyCharm
@file: __init__.py
@time: 17/8/14 19:39
@desc:
'''
from flask import Flask

app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'itcast'
    from .main import main as main_blueprint
    from .api import api as api_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_blueprint)
    return app

