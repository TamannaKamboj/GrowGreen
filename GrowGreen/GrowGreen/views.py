from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from .models import *


def home(request):
	return render (request,'index.html')

def blog(request):
	return render(request, 'blog.html')

def blog_details(request):
	return render(request, 'blog-details.html')

def contact(request):
	return render(request, 'contact-one.html')

def about(request):
	return render(request, 'about.html')

# inheritance abhi ni karte wo bad main kar denge? kya kahti hai pahle edit karlete hai?haan ok
# dekh ek bar changes aur bata ?
# shi h boht itne ab mere laptop p krde copy fr  m bna l
# wait any idea for that forth point