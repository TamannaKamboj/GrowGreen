
from django.db import models
from django.contrib.auth.models import  AbstractUser, User

class Post(models.Model):
	no=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50)
	discription=models.TextField()
	Content=models.TextField()
	Author=models.CharField(max_length=50)
	image=models.ImageField(upload_to="post")


class Comment(models.Model):
    comment1=models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.id)

