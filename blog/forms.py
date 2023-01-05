from django.forms import ModelForm
from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['content']
class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password1')
        confirm_password = cleaned_data.get('password2')

        if  User.objects.filter(username=username).exists():
            raise ValidationError({"username": "user with given username already exists"})
        if password != confirm_password:
            raise ValidationError({"password": "Error, passwords do not match"})
        return cleaned_data
    def save(self):
        print("saving")
        user = User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password')
        )
        print(user)
        print(user.email)
        print(user.password)
        return user
class LoginForm(ModelForm):
    class Meta:
        model=User
        fields= ['username','password']
    def clean(self):
        # cleaned_data = super().clean()
        username = self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        return self.cleaned_data
