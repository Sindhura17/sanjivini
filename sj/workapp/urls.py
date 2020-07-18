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
path('eventreg/',views.eventreg,name='eventreg'),
path('add_patient/',views.add_patient,name='add_patient'),
path('aux/',views.aux,name='aux'),
path('update_rec/',views.update_rec,name='update_rec'),
path('viewdetails/',views.viewdetails,name='viewdetails'),
path('dreg/',views.dreg,name='dreg'),
path('face/',views.face,name='face'),
path('doc_logout/',views.doc_logout,name='doc_logout'),
path('ngo_logout/',views.ngo_logout,name='ngo_logout'),

]