from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from workapp.forms import docForm,ngoForm,eventForm,patientForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import doc,ngo,event

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
    return render(request,'workapp/sign_up.html',{'dform':dform,'nform':nform,'m':'Enter valid details'})

def register(request):
    did=request.session['did']
    dobj=doc.objects.filter(id=did)
    eobj=event.objects.all()
    don=dobj[0].name
    firstletter=don[0]
    if(ord(firstletter)>=97):
        firstletter=chr(ord(firstletter)-32)
    li=list(don)
    li[0]=firstletter
    don="".join(li)
    dobj[0].name=don
    dobj1=dobj[0]
    dobj1.name=don
    eobj1=eobj
    for i in eobj1:
        nobj=ngo.objects.get(id=i.org_id_id)
        nname=nobj.name
        cn=nobj.ph
        i.nname=nname
        i.ph=cn
    D={"doc":dobj1,"eve":eobj1}
    return render(request,'workapp/docpage.html',D)

def ngosign(request):
    nform=ngoForm(request.POST)
    if nform.is_valid():
        n=nform.save()
        request.session['nid'] = n.id
        return HttpResponseRedirect('/workapp/nregister')
    dform=docForm()
    nform=ngoForm()
    return render(request,'workapp/sign_up.html',{'dform':dform,'nform':nform,'m':'Enter valid details'})
    
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
    eobj=event.objects.filter(org_id=nid)
    non=nobj[0].name
    firstletter=non[0]
    if(ord(firstletter)>=97):
        firstletter=chr(ord(firstletter)-32)
    li=list(non)
    li[0]=firstletter
    non="".join(li)
    nobj[0].name=non
    nobj1=nobj[0]
    nobj1.name=non
    eform=eventForm()
    pform=patientForm()
    N={"ngo":nobj1,"eve":eobj,'eform':eform,'pform':pform}
    return render(request,'workapp/ngopage.html',N)


def eventpage(request):
    return render(request,'workapp/eventpage.html')

def eventreg(request):
    eform=eventForm(request.POST)
    if eform.is_valid():
        e=eform.save(commit=False)
        nid=request.session['nid']
        e.org_id_id=nid
        e.save()
        #return render(request,'workapp/ngopage.html',{'m':'Event registered'})
    return HttpResponseRedirect('/workapp/nregister')
    #eform=eventForm()
    #return render(request,'workapp/ngopage.html',{'eform':eform,'m':'Enter valid details'})


def add_patient(request):
    pform=patientForm(request.POST)
    if pform.is_valid():
        pform.save()
    return HttpResponseRedirect('/workapp/nregister')
    