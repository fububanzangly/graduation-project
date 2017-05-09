from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from favorite import models as favoritemoudle
from bookinfo import models
# -*- coding: utf-8 -*-
# Create your views here.
@login_required
def favorite(request):
    userID = request.user.id
    bookID = request.GET.get('bookID')
    count = 0
    id = favoritemoudle.favorite.objects.filter(userID=userID)
    for line  in  id:
        if int(line.bookID) == int(bookID):
            count = count+1
        else:
            pass
    if count==0:
        favoritemoudle.favorite.objects.create(userID=userID, bookID=bookID)
    else:
        pass
    allBookID =  favoritemoudle.favorite.objects.filter(userID=userID)
    favoritebook = []
    for line in allBookID:
        id = line.bookID
        favoritebook += models.bookinfo.objects.filter(id=id)

    return render(request,"favorite.html",{"favoritebook":favoritebook})

@login_required
def showpage(request):
    userID = request.user.id
    allBookID = favoritemoudle.favorite.objects.filter(userID=userID)
    favoritebook = []
    for line in allBookID:
        id = line.bookID
        favoritebook += models.bookinfo.objects.filter(id=id)
    return render(request, "favorite.html",{"favoritebook":favoritebook})
@login_required
def showpage(request):
    userID = request.user.id
    allBookID = favoritemoudle.favorite.objects.filter(userID=userID)
    favoritebook = []
    for line in allBookID:
        id = line.bookID
        favoritebook += models.bookinfo.objects.filter(id=id)
    return render(request, "favorite.html",{"favoritebook":favoritebook})
def delFavorite(request):
    userID = request.user.id
    bookID = request.GET.get('bookID')
    favoritemoudle.favorite.objects.filter(userID=userID,bookID=bookID).delete()
    allBookID = favoritemoudle.favorite.objects.filter(userID=userID)
    favoritebook = []
    for line in allBookID:
        id = line.bookID
        favoritebook += models.bookinfo.objects.filter(id=id)
    return render(request, "favorite.html", {"favoritebook": favoritebook})
