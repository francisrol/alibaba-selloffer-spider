# -*- coding: utf-8 -*-

# Scrapy settings for alibaba project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'alibaba'

SPIDER_MODULES = ['alibaba.spiders']
NEWSPIDER_MODULE = 'alibaba.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'alibaba (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    # ":authority":"www.1688.com",
    #":method":"GET",
    #":path":"/",
    #":scheme":"https",
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    # "accept-encoding":"gzip, deflate, br",
    "accept-language":"zh-CN,zh;q=0.8",
    "cache-control":"no-cache",
    "cookie":'UM_distinctid=15d4e85fdf23e5-038937142195da-3065780b-1fa400-15d4e85fdf3749; ali_beacon_id=14.130.112.2.1500261115379.449555.9; h_keys="%u538b%u529b%u4eea%u8868#2017%u590f%u5b63%u5973%u58ebt%u6064#%u5973%u88c5#%u5b88%u671b%u5148%u950b#%u53d8%u5f62%u91d1%u521a#%u5316%u5986%u54c1"; CNZZDATA1261011362=137713964-1500259993-%7C1501509201; JSESSIONID=9L78Cedu1-UG8YXTFWhvTbUH6Su4-Y5Q8yQQ-fl; alicnweb=touch_tb_at%3D1501516865672; ad_prefer="2017/08/01 00:07:06"; ali_ab=14.130.112.2.1500260991070.8; isg=AtbWfQ9Fk97J16dpWi8XhIqCJ4oY3wVMqa_sTUA5ublUA36dqAZrwKox7akU; _csrf_token=1501517310260; cna=kenhESr003wCAQ6CcBHWGX5w; _tmp_ck_0="pgW8OZwgGvg%2FDIoFQVXmLCFrQaO%2Bwu0N7K7s8GbGT5vVMp5x73ChxwRzQolZ6t6zcIuYiXijK87nUAYlqKYkwN%2Fvur9ZpakE50qhNkXQMUQLoztx%2BL3Nd0glL2SeCEl7lh9m9e1IHm5mtA4NXlAwrQ5P1aYfLQoK%2FJwaiCmv85%2FxsFuJNBo4nvEC3hJ66rIxon2jXFjQcdlKwvPt3Qyl%2Fs5%2FVYvUyY65bBFVC0bUXYJ%2Fxu7gQQnUAYGabr7ypktfcmOyFkare4IY2MuCJ9wTCkzAtlKJbPkZLShitiotFZQwnDlDZUU2unLjs5ZYLEtKTPUxz52wg%2FLmKb9%2F7inYnA%3D%3D"',
    "pragma":"no-cache",
    "upgrade-insecure-requests":"1",
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'alibaba.middlewares.AlibabaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'alibaba.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'alibaba.pipelines.AlibabaCategoryPipeline': 300,
    'alibaba.pipelines.AlibabaSellofferPipeline': 400,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

SPIDER_PARAMS = {}

