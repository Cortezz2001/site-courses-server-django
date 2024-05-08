from rest_framework import serializers
from .models import Mentor, LearnedCourse


class MentorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Mentor
    fields = '__all__'  


class CourseSerializer(serializers.ModelSerializer):
  class Meta:
    model = LearnedCourse
    fields = '__all__'  


class NestedMentorSerializer(serializers.ModelSerializer):
  courses = CourseSerializer(source='course_set', many=True)

  class Meta:
    model = Mentor
    fields = '__all__'