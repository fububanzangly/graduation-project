from django.contrib import admin
#coding=utf8
# Register your models here.
from models import bookinfo,gitbook
class bookinfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'type', 'ISBN')
    search_fields = ('name', 'author', 'type', 'ISBN')
    list_filter = ('author', 'type',)
class gitbookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')
    search_fields = ('name', 'author')
    list_filter = ('name', 'author')



admin.site.register(bookinfo,bookinfoAdmin)
admin.site.register(gitbook,gitbookAdmin)
