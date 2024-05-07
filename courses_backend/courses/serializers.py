from rest_framework import serializers
from .models import Course, Skill, Control, Mentor, Theme, Features, Knowhow, Challenge


class CourseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Course
    fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
  class Meta:
    model = Skill
    fields = '__all__'


class ControlSerializer(serializers.ModelSerializer):
  class Meta:
    model = Control
    fields = '__all__'


class MentorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Mentor
    fields = '__all__'


class ThemeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Theme
    fields = '__all__'


class FeatureSerializer(serializers.ModelSerializer):
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
  skills = SkillSerializer(many=True)
  controls = ControlSerializer(many=True)
  mentors = MentorSerializer(many=True)
  themes = ThemeSerializer(many=True)
  features = FeatureSerializer(many=True)
  knowhows = KnowhowSerializer(many=True)
  challenges = ChallengeSerializer(many=True)


  class Meta:
    model = Course
    fields = '__all__'


