from django.shortcuts import render
from bookinfo import models
# Create your views here.
# -*- coding: utf-8 -*-
def show(request):
    name = request.GET.get('name')
    bookinfo = models.bookinfo.objects.all()
    infomation = models.bookinfo.objects.get(name= name)
    return render(request,'show.html',{'bookinfo':bookinfo,'infomation':infomation})