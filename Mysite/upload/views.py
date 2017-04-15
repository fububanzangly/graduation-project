from django.shortcuts import render
from bookinfo import models
import qiniu
import json
from django.http import JsonResponse
# Create your views here.
# coding=utf-8
from django.http import HttpResponse
import os
import douban_API
QINIU_ACCESS_KEY = 'V3Ki7ai3BF3yFhKO1KMOd_8LUmS_4bMdQbZvA93O'
QINIU_SECRET_KEY = 'KEMTQLLjydUWIQFA3NF4Sbjsv2RVl_tvwv3aw4Kc'
QINIU_BUCKET = 'book'



def uploadBooks(request):

#    if request.method == "POST":
#        myFile =request.FILES.get("myfile", None)
#        if not myFile:
#            return HttpResponse("no files for upload!")
#        bookname = myFile
#        douban_API.douban(bookname)
#        destination = open(os.path.join('/Users/liyang/Documents/Python/graduation-project/Mysite/static/upload',myFile.name),'wb+')
#        for chunk in myFile.chunks():
#            destination.write(chunk)
#        destination.close()
#        return HttpResponse("upload over!")
#    else :
#       return render(request, 'upload.html', locals())
    return render(request, 'upload.html')

def writeIntoDatabase(name,author,pubdate,type,ISBN,realpath):
    models.bookinfo.objects.create(name=name,author=author,pubdate=pubdate,type=type,ISBN=ISBN,path=realpath)
def token(request):
    q = qiniu.Auth(QINIU_ACCESS_KEY, QINIU_SECRET_KEY)
    token = q.upload_token(QINIU_BUCKET)
    return JsonResponse({'token':token})
