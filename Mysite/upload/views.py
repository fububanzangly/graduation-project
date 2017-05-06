from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from bookinfo import models
import qiniu
import json
# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.http import HttpResponse
import os
import urllib2
import douban_API
QINIU_ACCESS_KEY = 'V3Ki7ai3BF3yFhKO1KMOd_8LUmS_4bMdQbZvA93O'
QINIU_SECRET_KEY = 'KEMTQLLjydUWIQFA3NF4Sbjsv2RVl_tvwv3aw4Kc'
QINIU_BUCKET = 'book'
@login_required

def uploadBooks(request):
    return render(request, 'upload.html')

def writeIntoDatabase(name,author,pubdate,type,ISBN,realpath):
    models.bookinfo.objects.create(name=name,author=author,pubdate=pubdate,type=type,ISBN=ISBN,path=realpath)
def token(request):
    q = qiniu.Auth(QINIU_ACCESS_KEY, QINIU_SECRET_KEY)
    token = q.upload_token(QINIU_BUCKET)
    uptoken = {'uptoken':token}
    return HttpResponse(json.dumps(uptoken))
def getInfo(request):
    if request.is_ajax() and request.method == 'POST':
        dic_json = json.dumps(request.POST)
        resInfo = json.loads(dic_json)
        fileInfo =  resInfo["response"]
        bookinfo = eval(fileInfo)
        bookname = bookinfo["key"]
        douban_API.douban(bookname)
    return render_to_response('index.html')