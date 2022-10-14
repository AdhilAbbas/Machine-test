from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username= models.CharField(max_length=200,null=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']