from . import views
from django.urls import path,include
from django.conf.urls import url

urlpatterns=[
path('sign_Up/',views.sign_in,name='sign_in'),
path('docsign/',views.docsign,name='docsign'),
path('ngosign/',views.ngosign,name='ngosign'),
path('register/',views.register,name='register'),
path('nregister/',views.register,name='nregister'),
]