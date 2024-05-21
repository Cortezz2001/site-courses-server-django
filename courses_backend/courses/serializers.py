from rest_framework import serializers
from .models import Course, Skill, Program, Features, Knowhow, Challenge

from mentors.serializers import MentorSerializer


class CourseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Course
    fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
  class Meta:
    model = Skill
    fields = '__all__'


class ProgramSerializer(serializers.ModelSerializer):
  class Meta:
    model = Program
    fields = '__all__'


class FeaturesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Features
    fields = '__all__'


class KnowhowSerializer(serializers.ModelSerializer):
  class Meta:
    model = Knowhow
    fields = '__all__'


class ChallengeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Challenge
    fields = '__all__'


# Nested serializer for including related models within a CourseSerializer
class NestedCourseSerializer(serializers.ModelSerializer):
  skills = SkillSerializer(source='skill_set', many=True)  # Using 'source' for clarity
  active_mentors = MentorSerializer(many=True)
  programs = ProgramSerializer(source='program_set',many=True)
  features = FeaturesSerializer(source='features_set',many=True)
  knowhows = KnowhowSerializer(source='knowhow_set', many=True)
  challenges = ChallengeSerializer(source='challenge_set', many=True)

  class Meta:
    model = Course
    fields = '__all__'


