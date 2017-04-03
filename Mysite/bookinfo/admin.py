from django.contrib import admin

# Register your models here.
from bookinfo import models
admin.site.register(models.bookinfo)
admin.site.register(models.gitbook)
