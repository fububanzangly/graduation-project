from django.shortcuts import render
from bookinfo import models
# Create your views here.
name="Docker"
def show(request):
   # bookinfo = models.bookinfo.objects.all()
    #showinfomation(name)
    return render(request, 'show.html')
def showinfomation(name):
    infomation = models.bookinfo.objects.get(name=name)
    return ( {'infomation': infomation})