from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from workapp.forms import docForm,ngoForm

# Create your views here.
'''class sign_in(TemplateView):
    template_name='workapp/sign_in.html'
    
    def get(self,request):
        dform=docForm()
        nform=ngoForm()
        
        return render(request,self.template_name,{'dform':dform,'nform':nform})'''
def sign_in(request):
    dform=docForm()
    nform=ngoForm()
    return render(request,'workapp/sign_in.html',{'dform':dform,'nform':nform})
        
