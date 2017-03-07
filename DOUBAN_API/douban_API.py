# -*- coding: utf-8 -*-
import urllib
import urllib2

doubanAPI = "https://api.douban.com/v2/book/search"
q = "三生三世十里桃花"
count = "1"
url = doubanAPI+"?"+"q"+"="+q+"&"+"count"+"="+count
print url
req = urllib2.Request(url)
print req

res_data = urllib2.urlopen(req)
res = res_data.read()
print res