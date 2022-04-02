from django.shortcuts import render,redirect,get_object_or_404
from instagram.models import Comment, Post, Profile
from instagram.forms import CommentForm, NewPostForm, SignUpForm, UpdateProfileForm, UpdateUserForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives, send_mail
from django.conf import settings

# Create your views here.
@login_required(login_url='/accounts/login/')
def display_home(request):

    posts = Post.objects.all()
    profile = Profile.objects.all()
    comment = Comment.objects.all()
    return render(request,'index.html',{"posts":posts,"profile":profile,"comment":comment})
