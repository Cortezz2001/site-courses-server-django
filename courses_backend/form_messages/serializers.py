from rest_framework import serializers
from .models import FormMessage

class FormMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormMessage
        fields = '__all__'