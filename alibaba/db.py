#!/usr/bin/env python
# encoding=utf-8

'''
@author: Francis

@license: (C) Copyright 2017
@contact: ryomawithlst@sina.com
@software: PyCharm
@file: mongo.py
@time: 17/8/1 00:54
@desc:
'''
import pymysql
from config import MYSQLCONFIG

class MysqlHandler(object):

    def __init__(self):
        self.connect = pymysql.connect(**MYSQLCONFIG)

    def insert(self, sheet, columns, params):
        '''插入数据'''
        columns = ','.join(columns)
        values = ','.join(["%s"]*len(params))
        sql = "INSERT INTO {sheet}({columns}) VALUES({values})".format(
            sheet=sheet, columns=columns, values=values
        )
        cursor = self.execute(sql, params)
        cursor.close()

    def updateOrInsert(self, sheet, columns, params, where):
        '''更新或者插入(如果没有)数据'''
        values1 = ["%s"] * len(params)
        # 更新
        new_values = ','.join(['='.join(v) for v in zip(columns, values1)])
        update_sql = "UPDATE {sheet} SET {new_values} {where}".format(sheet=sheet, new_values=new_values, where=where)
        cursor=self.connect.cursor()
        result = cursor.execute(update_sql, params)
        if result != 0:
            return
        # 插入
        columns = ','.join(columns)
        values2 = ','.join(["%s"] * len(params))
        insert_sql = "INSERT INTO {sheet}({columns}) VALUES({values})".format(
            sheet=sheet, columns=columns, values=values2
        )
        cursor = self.execute(insert_sql, params)
        cursor.close()

    def fetchAll(self, sheet, columns=[], where=''):
        '''查询多条'''
        columns = ','.join(columns) if columns else '*'
        sql = "SELECT {columns} FROM {sheet}"
        cursor = self.execute(sql.format(columns=columns, sheet=sheet)+where)
        result = cursor.fetchall()
        cursor.close()
        return result

    def fetchOne(self, sheet, columns=[], where=''):
        '''查询一条'''
        columns = ','.join(columns) if columns else '*'
        sql = "SELECT {columns} FROM {sheet}"
        cursor = self.execute(sql.format(columns=columns, sheet=sheet)+where)
        result = cursor.fetchone()
        cursor.close()
        return result

    def execute(self, sql, params=[]):
        '''执行并提交'''
        cursor = self.connect.cursor()
        cursor.execute(sql, params)
        self.connect.commit()
        return cursor

    def __del__(self):
        self.connect.close()


class RedisHandler(object):
    pass

#mysqlClient = MysqlHandler()
error = pymysql.err