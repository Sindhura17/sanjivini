from . import views
from django.urls import path,include
from django.conf.urls import url

urlpatterns=[
path('sign_up/',views.sign_up,name='sign_up'),
path('docsign/',views.docsign,name='docsign'),
path('ngosign/',views.ngosign,name='ngosign'),
path('register/',views.register,name='register'),
path('nregister/',views.nregister,name='nregister'),
path('ngosign_in/',views.ngosign_in,name='ngosign_in'),
path('docsign_in/',views.docsign_in,name='docsign_in'),
path('eventpage/',views.eventpage,name='eventpage'),
]