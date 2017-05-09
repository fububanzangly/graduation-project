# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

# Create your models here.

class pic(models.Model):
    num = models.IntegerField(u'序号')
    path = models.CharField(u'文件名',max_length=200,default="/")
    def __unicode__(self):
        return self.path
