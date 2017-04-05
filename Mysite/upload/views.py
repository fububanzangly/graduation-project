from django.shortcuts import render
from bookinfo import models
# Create your views here.
# coding=utf-8
from django.http import HttpResponse
import os
import douban_API
def uploadBooks(request):
    if request.method == "POST":
        myFile =request.FILES.get("myfile", None)
        if not myFile:
            return HttpResponse("no files for upload!")
        bookname = myFile
        douban_API.douban(bookname)
        destination = open(os.path.join("/Users/liyang/Documents/Python/graduation-project/Mysite/upload/upload",myFile.name),'wb+')
        for chunk in myFile.chunks():
            destination.write(chunk)
        destination.close()
        return HttpResponse("upload over!")
    else :
        return render(request, 'uploadBooks.html', locals())
def writeIntoDatabase(name,author,pubdate,type,ISBN):
    models.bookinfo.objects.create(name=name,author=author,pubdate=pubdate,type=type,ISBN=ISBN)