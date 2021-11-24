from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from .models import *


def home(request):
	return render (request,'index.html')


 