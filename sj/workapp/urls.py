from . import views
from django.urls import path,include
from django.conf.urls import url

urlpatterns=[
path('sign_in/',views.sign_in,name='sign_in'),
]