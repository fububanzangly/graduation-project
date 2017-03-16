from django.shortcuts import render

# Create your views here.
# coding=utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
@csrf_exempt
@csrf_protect
def uploadBooks(request):
    from django import forms
    class UploadFileForm(forms.Form):
        title = forms.CharField(max_length=1000000)
        file = forms.FileField()
    if request.method == "GET":
        data='get'
        print 'GET'
    if request.method == "POST":
        f = handle_uploaded_file(request.FILES['t_file'])
    return render_to_response('upload.html')
    #return HttpResponse(data)
def handle_uploaded_file(f):
    f_path='/'+f.name
    with open(f_path, 'wb+') as info:
        print f.name
        for chunk in f.chunks():
            info.write(chunk)
    return f