# -*- coding: utf-8 -*-
import urllib2
import json
doubanAPI = "https://api.douban.com/v2/book/search"
#q = raw_input('请输入查询书名')
q = "用python写网络爬虫"
count = 1
url = '%s?q=%s&count=%d'%(doubanAPI,q,count)
req = urllib2.Request(url)
res_data = urllib2.urlopen(req)
res = res_data.read()
dic_json = json.loads(res)
dicbook = dic_json["books"]
pubdate =   str(dicbook[0]["pubdate"])
name = q
for type in dic_json['books'][0]['tags'] :
    pass
type = type['name']
for author in dic_json["books"][0]['author']:
    pass