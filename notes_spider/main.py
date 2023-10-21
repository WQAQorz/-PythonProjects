import numpy as np
from common_tools.web_spider import WebSpider
from common_tools.matplot_tools import *

spider = WebSpider()

# 登录
spider.login()

# 获取网页源码进行解析
spider.get_source()
spider.parse()
