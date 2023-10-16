from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.

def landing(request):
    return render(
        request,
        'single_pages/landing.html'
    )
def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )