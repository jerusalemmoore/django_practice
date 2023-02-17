from django.shortcuts import render,  get_object_or_404
from itertools import chain
from .serializers import UserSerializer
from django.core import serializers
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Post, Follower
from .forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from .functions import *
from bootstrap_modal_forms.generic import BSModalUpdateView

# view that users land on if logged in or if anonymous user wants to view


def mainFeed(request):
    loggedUser = get_object_or_404(User, id=request.user.id)
    users = User.objects.all()
    serializedUsers = serializers.serialize("json", users)
    posts = Post.objects.all().order_by('-pub_date')
    if request.method == 'POST':
        userSearchForm = UserSearchForm(request.POST)
        if userSearchForm.is_valid():
            value = userSearchForm.data['username']
            return HttpResponseRedirect(reverse('home', kwargs={'id': User.objects.get(username=value).pk}))
    else:
        userSearchForm = UserSearchForm()
    context = {'posts': posts, 'loggedUser': loggedUser,
               'userSearchForm': userSearchForm, 'serializedUsers': serializedUsers}

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
                return HttpResponseRedirect(reverse('home', kwargs={'id': user.id}))
    else:
        loginForm = LoginForm()
    context = {'loginForm': loginForm}
    return render(request, 'blog/landing.html', context)
# view with form for creating new user


def registration(request):
    if request.method == 'POST':
        registrationForm = UserCreationForm(data=request.POST)
        if registrationForm.is_valid():
            user = registrationForm.save()
            login(request, user)
            return HttpResponseRedirect(reverse('home', kwargs={"id": user.id}))
    else:
        registrationForm = RegistrationForm()
    context = {'registrationForm': registrationForm}
    return render(request, 'blog/registration.html', context)


def logoutView(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect(reverse('landing'))

# @login_required


def home(request, id, postid=None):
    # serializedUsers = serializers.serialize("json", User.objects.all())
    # print(serializedUsers)
    if request.user.is_authenticated:
        loggedUser = get_object_or_404(User, id=request.user.id)
    else:
        loggedUser = None
   
        
    # for searchbar
    users = User.objects.all()
    serializedUsers = serializers.serialize("json", users)
    # serializedPosts = serializers.serialize("json", )
    # print(serializedUsers)
    # for user home info
    user = User.objects.get(pk=id)
    # users follower info
    following = user.following.all()
    followers = user.followed_by.all()
    allposts = retrieveAllPosts(user)
    postForm = PostForm()
    postUpdateForm = PostForm()
    userSearchForm = UserSearchForm()
    # if we redirected to home with a postid, assume its to update a specific post in a modal and provide an instance
    if postid and request.method=='GET':
        postInstance = get_object_or_404(Post, id=postid)
        print(postInstance)
        postUpdateForm = PostForm(instance=postInstance)
        print(postUpdateForm)
    else:
        postUpdateForm = PostForm()

    if request.method == 'POST':
        # to verify what form i'm submitting read the names what was pressed
        if 'addPostSubmit' in request.POST:
            postForm = PostForm(request.POST)
            if postForm.is_valid():
                post = postForm.save(commit=False)
                post.user = user
                post.save()
                return HttpResponseRedirect(reverse('home', kwargs={'id': user.id}))
        elif 'postUpdateSubmit' in request.POST:
            postInstance = get_object_or_404(Post, id=postid)
            postUpdateForm = PostUpdateForm(request.POST, instance=postInstance)
            if postUpdateForm.is_valid():
                postUpdateForm.save()
                return HttpResponseRedirect(reverse('home', kwargs={'id': user.id}))
        # last case assumes we submitted the user search form, can use convention above because of difference in how 
        # the user search form doesn't have a submit button
        else:
            userSearchForm = UserSearchForm(request.POST)
            if userSearchForm.is_valid():
                
                value = userSearchForm.data['username']
                return HttpResponseRedirect(reverse('home', kwargs={'id': get_object_or_404(User,username=value).pk}))
    else:
        postForm = PostForm()
        userSearchForm = UserSearchForm()
        # this caused the update form to be blank when opening modal
        # postUpdateForm = PostForm()

    context = {'loggedUser': loggedUser,
               'user': user, 'postForm': postForm,
               'followers': followers, 'following': following,
               'users': users,
               'userSearchForm': userSearchForm,
               'allposts': allposts,
               'serializedUsers': serializedUsers,
               'postUpdateForm': postUpdateForm}

    return render(request, 'blog/home.html', context)


def unfollow(request, id):
    loggedUser = get_object_or_404(User, id=request.user.id)
    user = User.objects.get(pk=id)
    loggedUserAsFollower = user.followed_by.get(user=loggedUser)
    loggedUserAsFollower.delete()
    return HttpResponseRedirect(reverse('home', kwargs={'id': user.id}))


def follow(request, id):
    loggedUser = get_object_or_404(User, id=request.user.id)
    user = User.objects.get(pk=id)
    follower = Follower(user=loggedUser, following=user)
    follower.save()
    return HttpResponseRedirect(reverse('home', kwargs={'id': user.id}))

# pass the postid from /home/userid/updatePost/postid to /home/userid
def updatePost(request,id,postid):
    return HttpResponseRedirect(reverse('home', kwargs={'id': id, 'postid': postid}))
