
from django import forms
from .models import doc,ngo

class docForm(forms.Form):
    Username=forms.CharField()
    Password=forms.CharField(widget=forms.PasswordInput())
    Email=forms.EmailField()
    Name=forms.CharField()
    Phone=forms.CharField(max_length=10)
    City=forms.CharField()
    Specialization=forms.CharField()
    
    class meta():
        model=doc
        fields=("username","password","email","name","phone","city","special",)


class ngoForm(forms.ModelForm):
    Username=forms.CharField()
    Password=forms.CharField(widget=forms.PasswordInput())
    Email=forms.EmailField()
    Name=forms.CharField()
    Phone=forms.CharField(max_length=10)
    Website=forms.URLField()
    Description=forms.CharField(widget=forms.Textarea(attrs={"rows":5,"cols":20}))
    class Meta:
        model=ngo
        fields=('username','password','email','name','ph','link','text',)

