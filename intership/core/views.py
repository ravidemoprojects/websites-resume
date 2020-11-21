from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm, LoginForm, PostdoubtForm
from django.contrib.auth import authenticate, login, logout
from .models import Doubt
from django.contrib.auth.models import Group

# Create your views here.
def Core(request):
    return render(request, 'core/core.html')


def Home(request):
    return render(request, 'core/home.html')

def Login(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/dbt/')
            else:
                form = LoginForm()
        else:
            form = LoginForm()
        
        return render(request, 'core/login.html',{'form':form})
    
    else:
        return HttpResponseRedirect('/dbt/')
 
def Signup(request):
    if request.method =='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
            
    else:
        form = SignupForm()
    
    return render(request, 'core/signup.html',{'form':form})

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def Doubt_list(request):
    if request.user.is_authenticated:
        doubt = Doubt.objects.all()
        return render(request, 'core/doubts.html',{'doubt':doubt})
    else:
        return HttpResponseRedirect('/lgin/')

   
def AddDoubt(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            form = PostdoubtForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                desc = form.cleaned_data['desc']
                pst = Doubt(subject=subject, desc=desc)
                pst.save()
                form = PostdoubtForm()
            else:
                form = PostdoubtForm()
        else:
            form = PostdoubtForm()
        
        
        return render(request, 'core/adddoubts.html', {'form':form})
    else:
        return HttpResponseRedirect('/lgin/')
    