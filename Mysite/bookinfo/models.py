# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class bookinfo(models.Model):
    name = models.CharField(max_length=20,null=False)
    author = models.CharField(max_length=20)
    pubdate = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    ISBN = models.CharField(max_length=20)