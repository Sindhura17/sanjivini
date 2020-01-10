
from django import forms
from .models import doc,ngo

class docForm(forms.ModelForm):
    
    class Meta:
        model=doc
        fields=('username','password','email','name','phone','city','special',)
        widgets={
            'name':forms.TextInput(attrs={'class':"form-control"}),
            'username':forms.TextInput(attrs={'class':"form-control"}),
            'email':forms.TextInput(attrs={'class':"form-control"}),
            'password':forms.TextInput(attrs={'class':"form-control"}),
            'phone':forms.TextInput(attrs={'class':"form-control"}),
            'city':forms.TextInput(attrs={'class':"form-control"}),
            'special':forms.TextInput(attrs={'class':"form-control"}),
            }


class ngoForm(forms.ModelForm):
    '''Username=forms.CharField()
    Password=forms.CharField(widget=forms.PasswordInput())
    Email=forms.EmailField()
    Name=forms.CharField()
    Phone=forms.CharField()
    Website=forms.URLField()
    Description=forms.CharField(widget=forms.Textarea(attrs={"rows":5,"cols":20}))'''
    class Meta:
        model=ngo
        fields=('username','password','email','name','ph','link','text',)
        widgets={
            'name':forms.TextInput(attrs={'class':"form-control"}),
            'username':forms.TextInput(attrs={'class':"form-control"}),
            'email':forms.TextInput(attrs={'class':"form-control"}),
            'password':forms.TextInput(attrs={'class':"form-control"}),
            'ph':forms.TextInput(attrs={'class':"form-control"}),
            'link':forms.TextInput(attrs={'class':"form-control"}),
            'text':forms.Textarea(attrs={"rows":5,"cols":20}),
            }

