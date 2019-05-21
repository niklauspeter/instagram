from django.shortcuts import render, redirect
from django.http  import HttpResponse
from .models import Image

def welcome(request):
    image = Image.display_images()
    return render(request, 'all-posts/index.html', {"image":image})

# Create your views here.
def search_results(request):
    
    if 'post_item' in request.GET and request.GET["post_item"]:
        search_term = request.GET.get("post_item")
        searched_images = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-posts/search.html',{"message":message,"image": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-posts/search.html',{"message":message})