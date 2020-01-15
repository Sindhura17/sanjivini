from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from workapp.forms import docForm,ngoForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import doc,ngo

# Create your views here.

def sign_in(request):
    dform=docForm()
    nform=ngoForm()
    return render(request,'workapp/sign_in.html',{'dform':dform,'nform':nform})

def docsign(request):
    dform=docForm(request.POST)
    if dform.is_valid():
        d=dform.save()
        request.session['did'] = d.id       
    return HttpResponseRedirect('/workapp/register')

def register(request):
    return render(request,'home.html')

def ngosign(request):
    nform=ngoForm(request.POST)
    if nform.is_valid():
        n=nform.save()
        request.session['nid'] = n.id
    return HttpResponseRedirect('/workapp/nregister')

def nregister(request):
    return render(request,'ngopage.html')
