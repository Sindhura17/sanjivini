from django.db import models
from django.conf import settings
class doctor(models.Model):
    username = models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30)
    email=models.EmailField(max_length=254,default='null')
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    city=models.CharField(max_length=30)
    special=models.CharField(max_length=30)
    