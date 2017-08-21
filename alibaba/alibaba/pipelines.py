# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import urllib
from datetime import datetime
from xpinyin import Pinyin

from db import MysqlHandler, error


class AlibabaCategoryPipeline(object):

    def __init__(self):
        self.pinyin = Pinyin()
        self.db = MysqlHandler()

    def process_item(self, item, spider):
        # 判断是不是分类爬虫
        if spider.name == "category":
            # 获取数据库table名称
            sheet_name = item['sheet']
            # 父级分类
            parent = item.get("parent", "")
            # 字段
            columns = ["parent", "name", "link", "shortcut"] if parent else ["name", "link", "shortcut"]
            # 遍历每条分类信息
            for name,link in item["result"]:
                # 判断是父级分类，还是子集分类
                # 如果存在parent，那么就是子集分类，添加父级分类的信息
                params = [parent] if parent else []
                # 如果缺少http协议头，那么加上
                if not link.startswith('http'):
                    # 因为淘宝导航中部分连接没有协议头，需要手动加上
                    link = 'https:' + link
                # 子分类页面，如果链接无效，那么替换掉无效链接
                if 'selloffer' not in link and parent:
                    # 如果没有该字段，说明该分类链接无效，因此替换为通用查询链接
                    kw = urllib.urlencode({"keywords": name.encode("gbk")})
                    link = "https://s.1688.com/selloffer/offer_search.htm?{kw}&button_click=top&earseDirect=false&n=y".format(kw=kw)
                # 把链接全部替换为查找供应商的格式
                # company  -->   selloffer
                # company_search   --->   offer_search
                link = link.replace('selloffer', "company").replace("offer_search", "company_search")
                # 如果是子集分类，那么加上父级的名称，实现该字段的唯一性要求，便于查询
                name = (parent + '-' + name) if parent else name
                params.append(name)
                params.append(link)
                params.append(self.pinyin.get_pinyin(name, ""))
                # 插入数据
                try:
                    # db.insert(sheet_name, columns, params)
                    self.db.updateOrInsert(sheet_name, columns, params, "where shortcut='%s'"%params[-1])
                except error.IntegrityError as e:
                    print("Duplicate Key")

        return item


class AlibabaSellofferPipeline(object):

    def __init__(self):
        self.db = MysqlHandler()

    def process_item(self, item, spider):
        if spider.name == "selloffer":
            sheet_name = "selloffer"
            columns = [
                "name",
                "url",
                "shortcut",
                "business_model",
                "linkman",
                "landline_phone",
                "mobile_phone",
                "address",
                "zipcode",
                "category_id",
                "sub_category_id",
                "create_time",
            ]
            params = [
                item["name"],
                item["url"],
                item["shortcut"],
                item["business_model"],
                item["linkman"],
                item["landline_phone"],
                item["mobile_phone"],
                item["address"],
                item["zipcode"],
                item["category_id"],
                item["sub_category_id"],
                datetime.now()
            ]
            # db.insert(sheet_name, columns, params)
            self.db.updateOrInsert(sheet_name, columns, params, "where shortcut='%s' and category_id=%d and sub_category_id=%d" %(item["shortcut"],item["category_id"],item["sub_category_id"]))
        return item


