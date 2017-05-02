from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'uploadbooks',views.uploadBooks),
    url(r'token',views.token),
    url(r'getInfo',views.getInfo),
]