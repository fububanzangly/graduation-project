from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
 username = models.CharField(max_length=50,blank=False, null=False)
 password = models.CharField(max_length=50,blank=False, null=False)
 email = models.EmailField(blank=False, null=False)
 age = models.CharField(max_length=5,default=18)