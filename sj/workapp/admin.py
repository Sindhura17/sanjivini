from django.contrib import admin
from .models import doc,ngo,event,patient,medication,doregis
# Register your models here.
admin.site.register(doc)
admin.site.register(ngo)
admin.site.register(event)
admin.site.register(patient)
admin.site.register(medication)
admin.site.register(doregis)
