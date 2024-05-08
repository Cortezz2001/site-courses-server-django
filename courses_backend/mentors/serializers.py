from rest_framework import serializers
from .models import Mentor, Course

class MentorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Mentor
    fields = '__all__'  

class CourseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Course
    fields = '__all__'  

class NestedMentorSerializer(serializers.ModelSerializer):
  courses = CourseSerializer(many=True)  

  class Meta:
    model = Mentor
    fields = '__all__'