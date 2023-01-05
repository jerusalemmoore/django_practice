from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *
# Create your views here.
def mainFeed(request):
    if request.method == 'POST':
        postForm = PostForm(request.POST)
        if postForm.is_valid():
            postForm.save()
            return HttpResponseRedirect(reverse('mainFeed'))
    else:
        postForm = PostForm()
    posts = Post.objects.all().order_by('-pub_date')
    context = {'posts':posts, 'postForm': postForm}
    return render(request, 'blog/mainFeed.html', context)


def landing(request):
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)

        user = authenticate(request, username= request.POST['username'], password=request.POST['password'])
        if user is not None:
            return HttpResponseRedirect(reverse('mainFeed'))
    else:
        loginForm = LoginForm()
    context = {'loginForm' : loginForm}
    return render(request, 'blog/landing.html', context)

def registration(request):
    if request.method == 'POST':
        registrationForm = RegistrationForm(request.POST)
        if registrationForm.is_valid():
            # registrationForm.save()
            user = User.objects.create_user(
                registrationForm.cleaned_data['username'],
                registrationForm.cleaned_data['email'],
                registrationForm.cleaned_data['password1']
            )
            return HttpResponseRedirect(reverse('mainFeed'))
    else:
        registrationForm = RegistrationForm()
    context = {'registrationForm' : registrationForm}
    return render(request, 'blog/registration.html', context)
