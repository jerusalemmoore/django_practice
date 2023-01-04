from django.forms import ModelForm
from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['content']
class RegistrationForm(ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if  User.objects.filter(username=username).exists():

            raise ValidationError({"username": "user with given username already exists"})
        if password != confirm_password:
            raise ValidationError({"password": "Error, passwords do not match"})
        return cleaned_data
