from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render,redirect

# Create your views here.
class sign_in(TemplateView):
    template_name='workapp/sign_in.html'
    
    def get(self,request):
        dform=docForm()
        nform=ngoForm()
        return render(request,self.template_name,{'dform':dform,'nform':nform})
        
         