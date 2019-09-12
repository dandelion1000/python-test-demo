"""
@author：zxx
@filename：GetHtmlData.py
@create_time：
@markdown_intro:测试爬虫（以爬取'https://www.php.cn/js-tutorial.html'上的网页数据为例）
"""

# 步骤
# 1.确定要爬取数据的网址
# 2.获取该网址的源码
# 3.使用正则表达式去匹配网址的源码（匹配所需要的数据类型）
# 4.将爬取的数据保存至本地或者数据库

# -*- encoding:utf-8 -*-
import os
import urllib.request
# 导入正则匹配包
import re

url = "https://zhuanlan.zhihu.com/p/26019553"
html = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
imgRex = '<img src="(http.*?)"'
imgReList = re.compile(imgRex).findall(html)
titRex = r'<h2>([^</.*>]+)'
# 所有的标题
titleReList = re.compile(titRex).findall(html)
print(titleReList)
print(imgReList)
path = os.getcwd() + '/' + 'test'
os.makedirs(path)
for index in range(len(imgReList)):
    urllib.request.urlretrieve(imgReList[index], os.getcwd()+'/test/'+str(index)+'.png')
