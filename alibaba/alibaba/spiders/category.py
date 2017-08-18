# -*- coding: utf-8 -*-
import scrapy


# 下载分类信息
class CategorySpider(scrapy.Spider):
    name = 'category'
    allowed_domains = ['1688.com']
    start_urls = ['http://www.1688.com/']

    def parse(self, response):
        # 分类导航名称以及链接
        category = response.xpath("//ul[@id='nav-sub']/li/a")
        names = category.xpath("./text()").extract()
        links = category.xpath('./@href').extract()
        # 分类信息及其导航信息
        result = zip(names, links)
        yield {"result": result, "sheet": "category"}

        # 请求子页面
        for name, link in result:
            if not link.startswith('http'):
                link = 'https:' + link
            yield scrapy.Request(link, meta={"parent": name}, callback=self.parse_sub_categories)

    def parse_sub_categories(self, response):
        # 子分类导购分类信息
        parent_name = response.meta["parent"]
        sub_category = response.xpath("//div[@class='ch-menu-item-list']//li/a")
        names = sub_category.xpath('./text()').extract()
        links = sub_category.xpath('./@href').extract()
        result = zip(names, links)
        return {"result": result, "sheet": "sub_category", "parent": parent_name}

