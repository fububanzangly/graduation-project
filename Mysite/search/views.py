# -*- coding: utf-8 -*-
from django.shortcuts import render
from bookinfo import models
def search(request):
    keyword = request.GET.get('keyword')
    result = models.bookinfo.objects.filter(name__contains = keyword,isshow=1)
    gitresult = models.gitbook.objects.filter(name__contains=keyword,isshow=1)
    return render(request,'search.html',{'result':result,'gitresult':gitresult})
