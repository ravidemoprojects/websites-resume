from django.shortcuts import render, HttpResponseRedirect
from .forms import User_signupForm, LoginForm, Post_form 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User_post
from django.contrib.auth.models import Group

# Create your views here.
""" Home """

def home(request):
    posts =User_post.objects.all()
    return render(request,'Blog/home.html',{'posts':posts})

""" About view """

def about(request):
    return render(request,'Blog/about.html')


""" Contact Us view """

def contact(request):
    return render(request,'Blog/contact.html')


""" Dashboard view """

def dashboard(request):
    if request.user.is_authenticated:
        posts = User_post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request,'Blog/dashboard.html',{'posts':posts,'full_name':full_name,'groups':gps})
    else:
        return HttpResponseRedirect('/login/')
    


""" Signup view """

def User_signup(request):
    if request.method =='POST':
        form = User_signupForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congrats you are an authoer now!')
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
        else:
            form = User_signupForm()
        return HttpResponseRedirect('/login/')
        
    else:
        form = User_signupForm()
    return render(request,'Blog/signup.html',{'form':form})


""" Login view """

def User_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/dashboard/')
                else:
                    form = LoginForm()
            else:
                form = LoginForm()
        else:
            form = LoginForm()
        return render(request,'Blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')


""" Logout view """

def User_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
    

""" add post by author """

def add_post(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            form = Post_form(request.POST)
            if form.is_valid():
                form.save()
               
            else:
                form = Post_form()
        else:
            form = Post_form()
        return render(request, 'Blog/addpost.html',{'form':form})        
    else:
        return HttpResponseRedirect('/login/')


""" update post by author """

def update_post(request, id):
    if request.user.is_authenticated:
        if request.method =='POST':
            pi = User_post.objects.get(pk=id)
            form = Post_form(request.POST, instance=pi)
            if form.is_valid():
                form.save()
            else:
                pi = User_post.objects.get(pk=id)
                form = Post_form(instance=pi)
        else:
                pi = User_post.objects.get(pk=id)
                form = Post_form(instance=pi)
        return render(request, 'Blog/updatepost.html')
    else:
        return HttpResponseRedirect('/login/')


""" delete post by author """

def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method =='POST':
            pi = User_post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
        
    else:
        return HttpResponseRedirect('/login/')

