from django.db import models

# Create your models here.
class doc(models.Model):
    username = models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    city=models.CharField(max_length=30)
    special=models.CharField(max_length=30)

class patient(models.Model):
    name=models.CharField(max_length=30)
    city=models.CharField(max_length=10)
    adhar_no=models.CharField(max_length=12,primary_key=True)
    phone=models.CharField(max_length=10)

class medication(models.Model):
    evevtdate=models.ForeignKey(event,on_delete=models.CASCADE)
    adhar_no=models.ForeignKey(patient,on_delete=models.CASCADE)
    desc=models.TextField()

