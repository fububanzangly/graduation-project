# -*- coding: utf-8 -*-
import json
import urllib2

import Database


def douban(bookname):
    doubanAPI = "https://api.douban.com/v2/book/search"
    q = bookname
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
    Database.writeIntoDataBase(name, author, pubdate, type);