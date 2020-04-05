from django.shortcuts import render, redirect, get_object_or_404
from .forms import postForm, registerForm, deleteForm
from .models import KobePost, registrationReviewer
from .autoCheck import checkPost
from .facebookApi import FbManger
from .postDeleteTokenCreater import createToken
from django.contrib import messages
import json

def home(request):
    return render(request, 'home.html', {})

def coc(request):
    return render(request, 'coc.html', {})

def about(request):
    return render(request, 'about.html', {})

def contribution(request):
    return render(request, 'contribution.html', {})

def registrationSuccess(request):
    return render(request, 'registrationSuccess.html', {})

def postlist(request):
    post = KobePost.objects.all()
    return render(request, 'postlist.html', {'post': post})

def registration(request):
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.registerIpAddress = str(getIp(request))
            if post.agreeCoc: # check coc policy
                post.save()
                return redirect('/registrationSuccess/')
            else:
                messages.warning(request, '請先閱讀並同意行為準則')
    else:
        form = registerForm()
    return render(request, 'registration.html', {'form': form})

def postSystem(request):
    if request.method == "POST":
        form = postForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.ipAddress = str(getIp(request))
            post.token = str(createToken.token())
            if post.cocPolicy: # check coc policy
                if checkPost.check(post.content) == True: #auto check post
                    if post.photo:
                        post.check = 'True'
                        post.save()
                        poster = FbManger(post, post.content, post.postTime) #post to facebook
                        post.postId = poster.imgPoster(post.photo)
                        post.checkPosted = 'True'
                        post.save()
                        return redirect('/postsuccess/' + str(post.id) + '/')
                    else:
                        post.check = 'True'
                        post.save()
                        poster = FbManger(post, post.content, post.postTime) #post to facebook
                        post.postId = poster.poster()
                        post.checkPosted = 'True'
                        post.save()
                        return redirect('/postsuccess/' + str(post.id) + '/')
                else:
                    post.save()
                    return redirect('/')
            else:
                messages.warning(request, '請先閱讀並同意行為準則')
    else:
        form = postForm()
    return render(request, 'post.html', {'form': form})

def postDelete(post_token):
    post = KobePost.objects.get(token = post_token) #get post by post token
    print(post.postId)
    poster = FbManger(post, post.content, post.postTime)
    poster.postDeleter(post.postId) #delete post

def deletePostSystem(request):
    if request.method == "POST":
        form = deleteForm(request.POST)
        if form.is_valid():
            deleteToken = form.cleaned_data['deleteToken']
            postDelete(deleteToken)
            return redirect('/')
    else:
        form = deleteForm()
    return render(request, 'deletepost.html', {'form': form})

def postSuccess(request, id):
    post = KobePost.objects.get(id = id)
    return render(request, 'postSuccess.html', {'post': post})

def getIp(request):
    xForwardedFor = request.META.get('HTTP_X_FORWARDED_FOR')
    if xForwardedFor:
        ip = xForwardedFor.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
