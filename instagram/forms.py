from django import forms
from django.contrib.auth.models import User
from instagram.models import Comment, Post, Profile
from django.contrib.auth.forms import UserCreationForm
class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required.')
    class Meta:
        model = User
        fields = ('username', 'email')
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']
