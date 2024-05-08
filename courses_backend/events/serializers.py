from rest_framework import serializers
from .models import Event
from mentors.serializers import MentorSerializer


class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = '__all__'


class NestedEventSerializer(serializers.ModelSerializer):
  active_mentors = MentorSerializer(many=True)

  class Meta:
    model = Event
    fields = '__all__'