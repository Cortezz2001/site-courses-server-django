from rest_framework import serializers
from .models import PaymentOperation


class PaymentOperationSerializer(serializers.ModelSerializer):
    course_purchased_title = serializers.SerializerMethodField()

    class Meta:
        model = PaymentOperation
        fields = '__all__'  # Include all fields

    def get_course_purchased_title(self, obj):
        # Assuming 'courses.Course' has a 'title' field
        return obj.course_purchased.title if obj.course_purchased else None

