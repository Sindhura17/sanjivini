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
        fields=("username","password","email","name","phone","city","special")
        
        

    