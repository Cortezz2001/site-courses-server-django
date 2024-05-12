from rest_framework import serializers
from .models import FormMessage

class FormMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormMessage
        fields = '__all__'

    def create(self, validated_data):
        email = validated_data.get('email')
        form_message, created = FormMessage.objects.get_or_create(email=email, defaults=validated_data)
        if not created:
            for attr, value in validated_data.items():
                setattr(form_message, attr, value)
            form_message.save()
        return form_message