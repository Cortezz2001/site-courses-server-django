from rest_framework import generics
from .models import Mentor
from .serializers import MentorSerializer, NestedMentorSerializer

class MentorListView(generics.ListAPIView):
  queryset = Mentor.objects.all()
  serializer_class = MentorSerializer

class MentorDetailView(generics.RetrieveAPIView):
  queryset = Mentor.objects.all()
  serializer_class = NestedMentorSerializer


class BriefMentorListView(generics.ListAPIView):
  queryset = Mentor.objects.all()
  serializer_class = MentorSerializer


  def get_queryset(self):
    queryset = super().get_queryset()
    return queryset.values('id', 'img', 'name', 'role')