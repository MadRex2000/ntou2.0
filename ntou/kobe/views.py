from django.shortcuts import render, redirect, get_object_or_404
from .forms import postForm
from .models import KobePost
from django.contrib import messages

def home(request):
    return render(request, 'home.html', {})

def coc(request):
    return render(request, 'coc.html', {})

def postSystem(request):

    if request.method == "POST":
        form = postForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = postForm()

    return render(request, 'post.html', {'form': form})
