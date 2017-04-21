# -*- coding: utf-8 -*-
import json
import urllib2
import views
def douban(bookname):
    doubanAPI = "https://api.douban.com/v2/book/search"
    q = bookname
    count = 1
    url = '%s?q=%s&count=%d'%(doubanAPI,q,count)
    path = 'http://oo8nzesko.bkt.clouddn.com/'
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    dic_json = json.loads(res)
    dicbook = dic_json["books"]
    pubdate = str(dicbook[0]["pubdate"])
    name_tmp = q.split('.')
    name = name_tmp[0]
    for type in dic_json['books'][0]['tags'] :
        pass
    type = type['name']
    for author in dic_json["books"][0]['author']:
        pass
    ISBN = dic_json["books"][0]['isbn10']
    realpath = str(path)+str(q)
    return views.writeIntoDatabase(name,author,pubdate,type,ISBN,realpath)
