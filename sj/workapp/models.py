from django.db import models

# Create your models here.
    
class ngo(models.Model):
    username=models.CharField(max_length=20,Unique=True)
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    name=models.CharField(max_length=30)
    ph=models.IntegerField(Unique=True)
    link=models.CharField(max_length=100)
    text=models.TextField(null=True)

class event(models.Model):
    name=models.CharField(max_length=50)
    venue=models.CharField(max_length=50)
    org_id=models.ForeignKey("ngo",on_delete=models.CASCADE,)
    city=models.CharField(max_length=40)
    nod=models.IntegerField(Default=0)
    date=models.DateField()
    time=models.TimeField(auto_now=False,auto_now_add=False)
    
class doregis(models.Model):
    evid=models.ForeignKey("event",on_delete=models.CASCADE)
    docid=models.ForeignKey("doc",on_delete=models.CASCADE)
    

