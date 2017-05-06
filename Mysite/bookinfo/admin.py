from django.contrib import admin
#coding=utf8
# Register your models here.
from models import bookinfo,gitbook
class bookinfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'type', 'ISBN')
    search_fields = ('name', 'author', 'type', 'ISBN')
    list_filter = ('author', 'type',)
class gitbookAdmin(admin.ModelAdmin):
    list_display = ('url', 'author')
    search_fields = ('url', 'author')
    list_filter = ('url', 'author')



admin.site.register(bookinfo,bookinfoAdmin)
admin.site.register(gitbook,gitbookAdmin)
