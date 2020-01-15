from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from workapp.forms import docForm,ngoForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import doc,ngo

# Create your views here.

def sign_up(request):
    dform=docForm()
    nform=ngoForm()
    return render(request,'workapp/sign_up.html',{'dform':dform,'nform':nform})

def docsign(request):
    dform=docForm(request.POST)
    if dform.is_valid():
        d=dform.save()
        request.session['did'] = d.id
        return HttpResponseRedirect('/workapp/register')
    dform=docForm()
    nform=ngoForm()
    return render(request,'workapp/sign_up.html',{'dform':dform,'nform':nform})

def register(request):
    return render(request,'home.html')

def ngosign(request):
    nform=ngoForm(request.POST)
    if nform.is_valid():
        n=nform.save()
        request.session['nid'] = n.id
        return HttpResponseRedirect('/workapp/nregister')
    dform=docForm()
    nform=ngoForm()
    return render(request,'workapp/sign_up.html',{'dform':dform,'nform':nform})
    
def ngosign_in(request):
    uname=request.POST.get("nusername")
    password=request.POST.get("npassword")
    nobj=ngo.objects.filter(username=uname)
    if not nobj:
        return HttpResponse("no username")
    if(nobj[0].password==password):
        return HttpResponse("found")
    else:
        return HttpResponse("not found")
        
def docsign_in(request):
    uname=request.POST.get("username")
    password=request.POST.get("password")
    dobj=doc.objects.filter(username=uname)
    if not dobj:
        return HttpResponse("no username")
    if(dobj[0].password==password):
        return HttpResponse("found")
    else:
        return HttpResponse("not found")
   

def nregister(request):
    return render(request,'home.html')
