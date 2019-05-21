from django.shortcuts import render, redirect
from django.http  import HttpResponse
from .models import Image

def welcome(request):
    image = Image.display_images()
    return render(request, 'all-posts/index.html', {"image":image})

# Create your views here.
