from rest_framework import generics
from .models import FormMessage
from .serializers import FormMessageSerializer

class FormMessageListCreate(generics.CreateAPIView):
    queryset = FormMessage.objects.all()
    serializer_class = FormMessageSerializer