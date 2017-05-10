from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
# coding=utf-8
from django.http import HttpResponse
import os

def homepage(request):
        from bookinfo import models
        bookinfo = models.bookinfo.objects.filter(isshow=1).order_by('-id')
        github = models.gitbook.objects.filter(isshow=1).order_by('-id')
        bookrecommend = models.bookinfo.objects.filter(isrecommend=1)
        recommend1 = models.bookinfo.objects.get(id=1)
        recommend2 = models.bookinfo.objects.get(id=2)
        recommend3 = models.bookinfo.objects.get(id=3)
        pic = getPicture
        return render(request,'index.html',{'bookinfo':bookinfo,
                                            'bookrecommend':bookrecommend,
                                            'recommend1':recommend1,
                                            'recommend2':recommend2,
                                            'recommend3': recommend3,
                                            'pic': pic,
                                            'github': github,
                                            })
@login_required
def changpicture(request):
        return render(request, 'changepic.html')
def getPicture():
    from models import pic
    pic = pic.objects.all()
    return pic