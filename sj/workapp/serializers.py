from rest_framework import serializers
from .models import doc,ngo,event,patient,medication

'''class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=event
        fields=['name','venue','city','maxd','date','time','text','img']'''

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=event
        fields='__all__'