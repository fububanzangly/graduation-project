from django.shortcuts import render
import pygit2
# Create your views here.

def uploadGitBook (url):
    pygit2.clone_repository(url)
