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
    did=request.session['did']
    dobj=doc.objects.filter(id=did)
    print(dobj[0].name)
    return render(request,'workapp/docpage.html')

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
        return render(request,'home.html')
    if(nobj[0].password==password):
        request.session['nid']=nobj[0].id
        return HttpResponseRedirect('/workapp/nregister')
    else:
        return render(request,'home.html')
        
def docsign_in(request):
    uname=request.POST.get("username")
    password=request.POST.get("password")
    dobj=doc.objects.filter(username=uname)
    if not dobj:
        return render(request,'home.html')
    if(dobj[0].password==password):
        request.session['did']=dobj[0].id
        return HttpResponseRedirect('/workapp/register')
    else:
        return render(request,'home.html')
   

def nregister(request):
    nid=request.session['nid']
    nobj=ngo.objects.filter(id=nid)
    print(nobj[0].name)
    return render(request,'workapp/ngopage.html')


def eventpage(request):
    return render(request,'workapp/evenpage.html')