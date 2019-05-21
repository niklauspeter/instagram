from django.shortcuts import render, redirect
from django.http  import HttpResponse


def welcome(request):
    return render(request, 'all-posts/index.html')

# Create your views here.
