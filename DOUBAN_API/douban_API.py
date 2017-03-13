# -*- coding: utf-8 -*-
import urllib
import urllib2

doubanAPI = "https://api.douban.com/v2/book/search"
q = raw_input('请输入查询书名')
count = 1
url = '%s?q=%s&count=%d'%(doubanAPI,q,count)
print url
req = urllib2.Request(url)
print req

res_data = urllib2.urlopen(req)
res = res_data.read()
print res