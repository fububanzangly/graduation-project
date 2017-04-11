from django.shortcuts import render
from bookinfo import models
import qiniu
# Create your views here.
# coding=utf-8
from django.http import HttpResponse
import os
import douban_API
from qiniu import Auth
def uploadBooks(request):
    if request.method == "POST":
        myFile =request.FILES.get("myfile", None)
        if not myFile:
            return HttpResponse("no files for upload!")
        bookname = myFile
        douban_API.douban(bookname)
        destination = open(os.path.join('/Users/liyang/Documents/Python/graduation-project/Mysite/static/upload',myFile.name),'wb+')
        for chunk in myFile.chunks():
            destination.write(chunk)
        destination.close()
        return HttpResponse("upload over!")
    else :
        return render(request, 'upload.html', locals())


def writeIntoDatabase(name,author,pubdate,type,ISBN,realpath):
    models.bookinfo.objects.create(name=name,author=author,pubdate=pubdate,type=type,ISBN=ISBN,path=realpath)
