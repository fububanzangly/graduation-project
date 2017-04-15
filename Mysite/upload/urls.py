from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'uploadBooks',views.uploadBooks),
   # url(r'/token',views.token),
]