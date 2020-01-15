
from django import forms
from .models import doc,ngo,event,patient

class docForm(forms.ModelForm):
    
    class Meta:
        model=doc
        fields=['name','username','email','password','phone','city','special']
        widgets={
            'name':forms.TextInput(attrs={'class':"form-control"}),
            'username':forms.TextInput(attrs={'class':"form-control"}),
            'email':forms.EmailInput(attrs={'class':"form-control"}),
            'password':forms.PasswordInput(attrs={'class':"form-control"}),
            'phone':forms.TextInput(attrs={'class':"form-control"}),
            'city':forms.TextInput(attrs={'class':"form-control"}),
            'special':forms.TextInput(attrs={'class':"form-control"}),
            }

class ngoForm(forms.ModelForm):
    '''Uername=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
    email=forms.EmailField()
    Name=forms.CharField()
    Phone=forms.CharField()
    Website=forms.URLField()
    Description=forms.CharField(widget=forms.Textarea(attrs={"rows":5,"cols":20}))'''
    class Meta:
        model=ngo
        fields=['name','username','email','password','ph','link','text']
        widgets={
            'name':forms.TextInput(attrs={'class':"form-control"}),
            'username':forms.TextInput(attrs={'class':"form-control"}),
            'email':forms.EmailInput(attrs={'class':"form-control"}),
            'password':forms.PasswordInput(attrs={'class':"form-control"}),
            'ph':forms.TextInput(attrs={'class':"form-control"}),
            'link':forms.URLInput(attrs={'class':"form-control"}),
            'text':forms.TextInput(attrs={'class':"form-control"}),
            }

class eventForm(forms.ModelForm):
    class Meta:
        model=event
        fields=['name','venue','city','maxd','date','time','text']
        widgets={
            'name':forms.TextInput(attrs={'class':"form-control"}),
            'venue':forms.TextInput(attrs={'class':"form-control"}),
            'city':forms.TextInput(attrs={'class':"form-control"}),
            'maxd':forms.NumberInput(attrs={'class':"form-control"}),
            'date':forms.DateInput(attrs={'class':"form-control"}),
            'time':forms.TimeInput(attrs={'class':"form-control"}),
            'text':forms.TextInput(attrs={'class':"form-control"}),
        }

class patientForm(forms.ModelForm):
    class Meta:
        model=patient
        fields=['name','city','adhar_no','phone']
        widgets={
            'name':forms.TextInput(attrs={'class':"form-control"}),
            'city':forms.TextInput(attrs={'class':"form-control"}),
            'adhar_no':forms.TextInput(attrs={'class':"form-control"}),
            'phone':forms.TextInput(attrs={'class':"form-control"}),
        }



