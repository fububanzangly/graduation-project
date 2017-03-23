from django.shortcuts import render
# Create your views here.
# coding=utf-8
from django.http import HttpResponse
import os

def homepage(request):
        return render(request, 'index.html', locals())