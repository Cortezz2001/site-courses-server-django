from rest_framework import generics
from .models import Event
from .serializers import EventSerializer, NestedEventSerializer


class EventListView(generics.ListAPIView):
  queryset = Event.objects.all()
  serializer_class = EventSerializer


class EventDetailView(generics.RetrieveAPIView):
  queryset = Event.objects.all()
  serializer_class = NestedEventSerializer

