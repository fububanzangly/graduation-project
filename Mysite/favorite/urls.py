from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^favorite/', views.favorite),
    url(r'^showpage/', views.showpage),
    url(r'^delfavorite/', views.delFavorite),
]