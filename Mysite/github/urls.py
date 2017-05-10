from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^uploadgithub/',views.uploadGitBook),
    url(r'^github/',views.GitBook)
]