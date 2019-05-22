from django.shortcuts import render, redirect
from django.http  import HttpResponse
from .models import Image, Profile
from django.contrib.auth.decorators import login_required 
from .forms import NewImageForm, SignupForm, ProfileForm

@login_required(login_url='/accounts/login/')
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


@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('welcome')
    else:
        form = NewImageForm()
    return render(request, 'all-posts/new_image.html', {"form": form})

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user=request.user
    if request.method =='POST':
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.username = current_user
            profile.save()

    else:
        form=ProfileForm()

    return render(request,'all-posts/edit_profile.html',{"form":form})



@login_required(login_url='/accounts/login/')
def profile(request):
    # current_user = request.user
    # current_user_id=request.user.id

    # form=CommentForm()
    # comments=Comment.objects.all()
    # comment_number=len(comments)
    # print(current_user)
    # # print(current_user_id)

    # post_id = None
    # if request.method == 'GET':
    #     post_id = request.GET.get('post_id')

    # likes = 0
    # if post_id:
    #     post = Post.objects.get(id=int(post_id))
    #     if post:
    #         likes = post.likes + 1
    #         post.likes =  likes
    #         post.save()
    #         print(likes)

    #     return redirect('profile.html')

    # try:
        # profile = Profile.objects.get(username=current_user)
        # image = Image.objects.filter(username_id=current_user_id)
        # title = profile.name
        # username = profile.username
        # image_number= len(image)
        # print(post_number)

    # except ObjectDoesNotExist:
    #     return redirect('edit-profile')


    return render(request,'all-posts/profile.html')
    
    # {"profile":profile,"image":image,"form":form,"image_number":image_number,"title":title,"username":username,"comments":comments,"comment_number":comment_number})