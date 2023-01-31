from django.shortcuts import render,  get_object_or_404
from itertools import chain

from django.core import serializers
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post,Follower
from .forms import *
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from .functions import *

# view that users land on if logged in or if anonymous user wants to view
def mainFeed(request):
    loggedUser = request.user

    posts = Post.objects.all().order_by('-pub_date')
    if request.method=='POST':
        userSearchForm = UserSearchForm(request.POST)
        if userSearchForm.is_valid():
            value=userSearchForm.data['usernamne']
            return HttpResponseRedirect(reverse('home', kwargs={'id':Users.objects.get(username=value).pk}))
    else:
        userSearchForm = UserSearchForm()
    context = {'posts':posts, 'loggedUser':loggedUser, 'userSearchForm': userSearchForm}

    return render(request, 'blog/mainFeed.html', context)

# view users hit when reaching site, allows login or traversal to registration view
def landing(request):
    user = request.user
    if user.is_authenticated:
        return HttpResponseRedirect(reverse('mainFeed'))
    if request.method == 'POST':
        loginForm = AuthenticationForm(data=request.POST)
        if loginForm.is_valid():
             username = request.POST['username']
             password = request.POST['password']
             user = authenticate(request, username=username, password=password)
             if user is not None:
                 login(request, user)
                 return HttpResponseRedirect(reverse('home', kwargs={'id':user.id}))
    else:
        loginForm = LoginForm()
    context = {'loginForm' : loginForm}
    return render(request, 'blog/landing.html', context)
# view with form for creating new user
def registration(request):
    if request.method == 'POST':
        registrationForm = UserCreationForm(data=request.POST)
        if registrationForm.is_valid():
            user = registrationForm.save()
            login(request,user)
            return HttpResponseRedirect(reverse('home',kwargs={"id":user.id}))
    else:
        registrationForm = RegistrationForm()
    context = {'registrationForm' : registrationForm}
    return render(request, 'blog/registration.html', context)
def logoutView(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect(reverse('landing'))

# @login_required
def home(request, id):
    # serializedUsers = serializers.serialize("json", User.objects.all())
    # print(serializedUsers)
    if request.user.is_authenticated:
        loggedUser = get_object_or_404(User,id=request.user.id)
    else:
        loggedUser = None
    # for searchbar
    users = User.objects.all()
    #for user home info
    user = User.objects.get(pk=id)
    # users follower info
    following = user.following.all()
    followers = user.followed_by.all()
    allposts = retrieveAllPosts(user)
    if request.method == 'POST':
        postForm = PostForm(request.POST)
        userSearchForm = UserSearchForm(request.POST)
        if postForm.is_valid():
            post = postForm.save(commit=False)
            post.user = user
            post.save()
            return HttpResponseRedirect(reverse('home', kwargs={'id':user.id}))
        elif userSearchForm.is_valid():
            print(User.objects.all())
            print("form")
            print()
            value = userSearchForm.data['username']
            # print(User.objects.get(username=userForm['username']).id)
            return HttpResponseRedirect(reverse('home', kwargs={'id':User.objects.get(username=value).pk}))
    else:
        postForm = PostForm()
        userSearchForm =UserSearchForm()
    # print(followers)
    # print(following)
    return render(request, 'blog/home.html', {'loggedUser':loggedUser,
    'user': user,'postForm': postForm,
     'followers':followers,'following':following,
     'users':users,
     'userSearchForm':userSearchForm,
     'allposts':allposts})

def unfollow(request, id):
    loggedUser = get_object_or_404(User,id=request.user.id)
    user = User.objects.get(pk=id)
    loggedUserAsFollower = user.followed_by.get(user=loggedUser)
    loggedUserAsFollower.delete()
    return HttpResponseRedirect(reverse('home', kwargs={'id':user.id}))
def follow(request,id):
    loggedUser = get_object_or_404(User,id=request.user.id)
    user = User.objects.get(pk=id)
    follower = Follower(user=loggedUser, following=user)
    follower.save()
    return HttpResponseRedirect(reverse('home', kwargs={'id':user.id}))
# def removePost(request,id):
#     post = get_object_or_404(Post,id=id)
#
