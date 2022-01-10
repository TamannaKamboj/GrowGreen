
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import *

# Create your views here.
def home(request):
	return render (request,'index.html')

def blog(request):
	posts=Post.objects.all()
	return render(request, 'blog.html',{'post':posts})

def blog_details(request,posts_id):

	post_detail = Post.objects.filter(no=posts_id).first()
	return render(request, 'blog-details.html',{'post_details': post_detail })

def comments(request):
	if request.method=='POST':
		comment=request.POST.get('comment')
		obj=Comment(comment1=comment,user=request.user)
		obj.save()
		print("cvhvhbjnknkhbhkjbkjv")
	return render(request,'blog.html')

	print("srdcfyhgbnjlkjgfhdgsfdhfvbjklmjhgf")
