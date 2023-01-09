from django.shortcuts import render,  get_object_or_404

from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
# view that users land on if logged in or if anonymous user wants to view
def mainFeed(request):
    loggedUser = request.user
    posts = Post.objects.all().order_by('-pub_date')
    context = {'posts':posts, 'loggedUser':loggedUser}
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
    if request.user.is_authenticated:
        loggedUser = get_object_or_404(User,id=request.user.id)
    else:
        loggedUser = None
    user = User.objects.get(pk=id)
    following = user.following.all()
    followers= user.followed_by.all()
    # following = Friend.objects.filter(user=user)
    posts = Post.objects.filter(user=user).order_by('-pub_date')

    if request.method == 'POST':
        postForm = PostForm(request.POST)
        if postForm.is_valid():
            post = postForm.save(commit=False)
            post.user = user
            post.save()
            return HttpResponseRedirect(reverse('home', kwargs={'id':user.id}))
    else:
        postForm = PostForm()
    # print(followers)
    # print(following)
    return render(request, 'blog/home.html', {'loggedUser':loggedUser,'user': user,'postForm': postForm,'posts':posts, 'followers':followers,'following':following})

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
