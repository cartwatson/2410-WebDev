import re
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

# ---- VIEWS ----
# TODO: HTML TO TEMPLATE W/ DYNAMIC PIECE
# HOME
def index(request):
    return render(request, 'blog/home.html')

# ARCHIVE
def archive(request):
    return render(request, 'blog/archive.html')

# SINGLE BLOG ENTRY 
def blog_post(request):
    return render(request, 'blog/entry.html')

# ADD COMMENT

