from django.db import models

# Create your models here.
class doc(models.Model):
    username = models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=10,unique=True)
    city=models.CharField(max_length=30)
    special=models.CharField(max_length=30)

class patient(models.Model):
    name=models.CharField(max_length=30)
    city=models.CharField(max_length=10)
    adhar_no=models.CharField(max_length=12,primary_key=True)
    phone=models.CharField(max_length=10)

class medication(models.Model):
    eventid=models.ForeignKey("event",on_delete=models.CASCADE)
    adhar_no=models.ForeignKey("patient",on_delete=models.CASCADE)
    desc=models.TextField()
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['eventid','adhar_no'],name='unique_desc'),
        ] 
    

    
class ngo(models.Model):
    username=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    name=models.CharField(max_length=30)
    ph=models.CharField(max_length=10,unique=True)
    link=models.CharField(max_length=100)
    text=models.TextField(null=True)

class event(models.Model):
    name=models.CharField(max_length=50)
    venue=models.CharField(max_length=50)
    org_id=models.ForeignKey("ngo",on_delete=models.CASCADE,)
    city=models.CharField(max_length=40)
    nod=models.IntegerField(default=0)
    maxd=models.IntegerField()
    date=models.DateField()
    time=models.TimeField(auto_now=False,auto_now_add=False)
    
    
class doregis(models.Model):
    evid=models.ForeignKey("event",on_delete=models.CASCADE)
    docid=models.ForeignKey("doc",on_delete=models.CASCADE)
    


