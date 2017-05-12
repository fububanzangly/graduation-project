from django.shortcuts import render
import os
from bookinfo import models
# Create your views here.

def uploadGitBook (request):
    address = request.GET.get('address')
    zipAddress = address+"/archive/master.zip"
    add = address.split('/')
    author = str(add[3])
    name = str(add[4])
    mdAddress = "https://raw.githubusercontent.com/"+author+'/'+name+"/master/README.md"
    path = "./static/upload/"+name+".zip"
    os.environ['zipAddress'] = str(zipAddress)
    os.environ['mdAddress'] = str(mdAddress)
    os.chdir("/Users/liyang/Documents/Python/graduation-project/Mysite/static/upload")
    os.system("wget $zipAddress")
    os.system("wget $mdAddress")
    os.renames("README.md",name+".md")
    os.renames("master.zip", name + ".zip")
    models.gitbook.objects.create(name=name,author=author,path=path,realpath=address)
    return render(request, 'success.html')
def GitBook (request):
    return render(request, 'github.html')