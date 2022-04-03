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
@login_required(login_url='/accounts/login/')
def add_comment(request,id):
    post_comment = Comment.objects.filter(post= id)
    images = Post.objects.filter(id=id).all()
    current_user = request.user
    profile = Profile.objects.get(user = current_user)
    image = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = image
            comment.user = profile
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()

    return render(request,'comments.html',{"form":form,"images":images,"comments":post_comment})
def show_profile(request):
    current_user= request.user
    images= Post.objects.filter(image_profile=current_user.id).all

    return render(request, 'registration/profile.html',{"images":images} )
    
@login_required(login_url='/accounts/login/')    
def update_profile(request,id):
    
    object1 = get_object_or_404(Profile,user_id=id)
    object2 = get_object_or_404(User,id=id)
    form = UpdateProfileForm(request.POST or None, instance = object1)
    form2 = UpdateUserForm(request.POST or None, instance = object2)
    if form.is_valid() and form2.is_valid():
        form.save()
        form2.save()
        return HttpResponseRedirect("/profile")
    
    return render(request, "registration/update_profile.html", {"form":form, "form2":form2})        