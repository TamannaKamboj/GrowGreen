from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate

from .models import *


def home(request):
    return render (request,'index.html')


def contact(request):
    return render(request, 'contact-one.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(username =username, password = password)
        if user==None:
            messages.error(request, 'Please Enter Correct Details')
            return HttpResponse('enter correct details')
            return render(request,'login.html')
        else:
            login(request, user)
    return render(request,'login.html')

def signup(request):
    
    if request.method=='POST':
        name = request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        obj=User.objects.create_user(username=name , email=email, password=password)
        obj.save()
        return redirect('/login')
    return render(request,'signup.html')
    



