from django.shortcuts import render
import pygit2
# Create your views here.

def uploadGitBook (request):

   address = request.GET.get('address')
   readmeAddress = address + "/README.MD"
   #pygit2.clone_repository(address)
   print readmeAddress
   return render(request, 'github.html')
#https://github.com/fububanzangly/FixLinux