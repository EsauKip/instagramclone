from django import forms
from django.contrib.auth.models import User
from instagram.models import Comment, Post, Profile
from django.contrib.auth.forms import UserCreationForm
class SignUpForm(UserCreationForm):
    email = forms.EmailField()