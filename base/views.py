from django.shortcuts import render, redirect
from .models import Blog
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def index(request):
    if request.method == 'POST':
        blog = Blog.objects.create(name=request.POST['name'], blog=request.POST['blog'])
    return render(request, 'homeblog.html', {
        'blogs': Blog.objects.all()
    })

def login(request):

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user is not None:
            auth_login(request,user)
            return redirect('index')    
    return render(request, 'bloglogin.html', {
    })

def logout(request):
    auth_logout(request)
    return redirect('login')