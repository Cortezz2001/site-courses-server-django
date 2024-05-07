from rest_framework import serializers
from .models import Event, Mentor

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = '__all__'  

class MentorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Mentor
    fields = '__all__'  

class NestedEventSerializer(serializers.ModelSerializer):
  mentors = MentorSerializer(many=True)  

  class Meta:
    model = Event
    fields = '__all__'