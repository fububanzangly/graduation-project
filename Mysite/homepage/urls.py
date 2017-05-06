from django.conf.urls import url
from . import views
urlpatterns = [
url(r'changepic',views.changpicture),
    url(r'',views.homepage),
]
