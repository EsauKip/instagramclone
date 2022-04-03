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
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']

            user = User.objects.create_user(username=username, email=email,password=password)
            subject = 'welcome to IC page'
            message = f'Hi {user.username}, thank you for registering in instagram clone.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail( subject, message, email_from, recipient_list )
            return HttpResponse('Thank you for registering with us')
    else:
        form = SignUpForm()
    return render(request, 'registration_form.html', {'form': form})
@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    profile=request.GET.get('profile')
    profile = Profile.objects.get(user = current_user)
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)        
        if form.is_valid():
            image=form.cleaned_data.get('image')
            caption=form.cleaned_data.get('caption')
            post = Post(image = image,image_caption= caption, image_profile=profile)
            post.save()  
        else:
            print(form.errors)
        return redirect('index')
    else:
        form = NewPostForm()

    return render(request, 'newpost.html')    
