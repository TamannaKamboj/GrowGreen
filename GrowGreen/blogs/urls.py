from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[

   path("blogs",views.blog,name="blog"),
   path("blog_details/<int:posts_id>",views.blog_details,name="blog_details"),
   path("comment",views.comments,name="comment"),
   ]