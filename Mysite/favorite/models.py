# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class favorite(models.Model):
    userID= models.IntegerField(u'用户ID',null=False)
    bookID = models.IntegerField(u'书籍ID',null=False)
