# -*- coding: utf-8 -*-
import re

import scrapy


class SellofferSpider(scrapy.Spider):
    name = 'selloffer'
    allowed_domains = ['1688.com']
    # 营业额：10w以下、10-50w、50-100w、100-500w、500-1000w、1000w以上
    annualRevenue = ["8,1", "9, 10, 1", "11,1", "2,12,3", "14", "5,15,16,17,6,7"]

    def start_requests(self):
        # 提取主分类信息
        category = self.settings["SPIDER_PARAMS"].get("CATEGORY")
        # 提取子分类信息
        sub_category = self.settings["SPIDER_PARAMS"].get("SUB_CATEGORY")
        # 查询主分类信息
        for revenue in self.annualRevenue:
            # 按照营业额分批获取商家列表，控制数量在3000以下，
            url = sub_category["link"] + "&annualRevenue=" + revenue
            yield scrapy.Request(
                url,
                meta={"category_id": category["id"],
                      "sub_category_id": sub_category["id"]
                      },
                callback=self.parse
            )

    def parse(self, response):
        # 提取下一页
        nextUrl = response.xpath("//a[@class='page-next']/@href").extract()

        if nextUrl:
            yield scrapy.Request(nextUrl[0], meta=response.meta, callback=self.parse)
        #
        links = response.xpath("//ul[@class='sm-company-list fd-clr'][1]//a[@class='sm-offerResult-areaaddress']/@href").extract()
        for link in links:
            yield scrapy.Request(link, meta=response.meta, callback=self.parse_info)

    def parse_info(self, response):
        # 店家名称
        name = response.xpath("//div[@class='contact-info']/h4/text()").extract_first().strip()
        # 联系人
        linkman = response.xpath("//div[@class='contact-info']//a[@class='membername']/text()").extract_first().strip()
        # 经营模式
        business_model = response.xpath("//span[@class='biz-type-model']/text()").extract_first().strip()
        # 详细信息
        desc_dt = response.xpath("//div[@class='contcat-desc']/dl/dt")
        desc_dd = response.xpath("//div[@class='contcat-desc']/dl/dd")
        desc_dt = [i.xpath("string(.)").extract_first().strip() for i in desc_dt]
        desc_dd = [i.xpath("string(.)").extract_first().strip() for i in desc_dd]
        desc_dt = [i.replace(u"\xa0", u'') for i in desc_dt]  # 替换源码中的 &nbsp;
        desc = dict(zip(desc_dt, desc_dd))

        landline_phone = desc.get(u"电话：", '') # 提取电话
        mobile_phone = desc.get(u"移动电话：", '') # 提取移动电话
        address = desc.get(u"地址：", '') # 提取地址
        zipcode = desc.get(u"邮编：", '') # 提取邮编

        # print(dir(response))
        # print("name: %s"%name)
        # print("linkman: %s"%linkman)
        # print("business_model: %s"%business_model)
        # print("landline_phone: %s"%landline_phone)
        # print("mobile_phone: %s"%mobile_phone)
        # print("address: %s"%address)
        # print("zipcode: %s"%zipcode)
        # print("name: %s"%name)
        # print("linkman: %s"%linkman)
        # print("url: %s"%response.url)
        # print("shortcut: %s"%re.match(".*?//(.*?)\..*", response.url).group(1))

        return {
            "name": name,
            "linkman": linkman,
            "business_model": business_model,
            "landline_phone": landline_phone,
            "mobile_phone": mobile_phone,
            "address": address,
            "zipcode": zipcode,
            "url": response.url,
            "shortcut": re.match(".*?//(.*?)\..*", response.url).group(1),
            "category_id": response.meta["category_id"],
            "sub_category_id": response.meta["sub_category_id"],
        }







