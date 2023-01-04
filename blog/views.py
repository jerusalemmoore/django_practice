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
        registrationForm = RegistrationForm(request.POST)
        if registrationForm.is_valid():
            print("valid")
            registrationForm.save()
            return HttpResponseRedirect(reverse('mainFeed'))
        else:
            print("invalid")
    else:
        registrationForm = RegistrationForm()
    context = {'registrationForm' : registrationForm}
    return render(request, 'blog/landing.html', context)
