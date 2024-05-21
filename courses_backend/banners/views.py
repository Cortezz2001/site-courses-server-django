from rest_framework import generics
from .models import Banner
from .serializers import BannerSerializer

class BannerListView(generics.ListAPIView):
  """
  API endpoint for retrieving a list of all courses.
  """
  queryset = Banner.objects.all()
  serializer_class = BannerSerializer