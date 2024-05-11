from rest_framework import generics
from .models import FormMessage
from .serializers import FormMessageSerializer

class FormMessageListCreate(generics.ListCreateAPIView):
    queryset = FormMessage.objects.all()
    serializer_class = FormMessageSerializer

class FormMessageRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = FormMessage.objects.all()
    serializer_class = FormMessageSerializer
