from django.db import models
from django.contrib.auth.models import  AbstractUser, User

class Post(models.Model):
	Pno=models.AutoField(primary_key=True)
	Pname=models.CharField(max_length=50)
	Pdiscription=models.TextField()
	PContent=models.TextField()
	PAuthor=models.CharField(max_length=50)




