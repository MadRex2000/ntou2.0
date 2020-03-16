from django.shortcuts import render, redirect, get_object_or_404
from .forms import postForm
from .models import KobePost
from .autoCheck import checkPost
from django.contrib import messages

def home(request):
    return render(request, 'home.html', {})

def coc(request):
    return render(request, 'coc.html', {})

def about(request):
    return render(request, 'about.html', {})

def postlist(request):
    post = KobePost.objects.all()
    return render(request, 'postlist.html', {'post': post})

def postSystem(request):

    if request.method == "POST":
        form = postForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            if checkPost.check(post.content) == True:
                post.check = 'True'
                post.save()
                return redirect('/')
            else:
                post.save()
                return redirect('/')
    else:
        form = postForm()

    return render(request, 'post.html', {'form': form})
