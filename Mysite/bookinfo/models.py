# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.

class bookinfo(models.Model):
    is_show = (
        (1, u'允许展示'),
        (2, u'不允许展示'),
    )
    is_recommend = (
        (1, u'推荐'),
        (2, u'不推荐'),
    )
    name = models.CharField(u'书名',max_length=150,null=False)
    author = models.CharField(u'作者',max_length=150)
    pubdate = models.CharField(u'出版日期',max_length=20)
    type = models.CharField(u'类型',max_length=20)
    ISBN = models.CharField(u'ISBN',max_length=20)
    path = models.CharField(u'路径',max_length=200,default="/")
    isshow = models.IntegerField(u'允许显示',choices=is_show, default=2)
    isrecommend = models.IntegerField(u'是否推荐',choices=is_recommend, default=2)

    def __unicode__(self):
        return self.name


class gitbook(models.Model):
    is_show = (
        (1, u'允许展示'),
        (2, u'不允许展示'),
    )
    is_recommend = (
        (1, u'推荐'),
        (2, u'不推荐'),
    )
    url = models.CharField(u'链接地址',max_length=50,null=False)
    author = models.CharField(u'作者',max_length=20)
    path = models.CharField(u'路径',max_length=100,default="/")
    isshow = models.IntegerField(u'允许显示', choices=is_show, default=2)
    isrecommend = models.IntegerField(u'是否推荐', choices=is_recommend, default=2)
    def __unicode__(self):
        return self.name