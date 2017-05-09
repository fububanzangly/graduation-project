from django.contrib import admin
#coding=utf8
from models import pic
class picAdmin(admin.ModelAdmin):
    list_display = ('num', 'path',)
    search_fields = ('num', 'path',)
    list_filter = ('num', 'path',)

admin.site.register(pic,picAdmin)

