from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer, NestedCourseSerializer


class CourseListView(generics.RetrieveAPIView):
  """
  API endpoint for retrieving a list of all courses.
  """
  queryset = Course.objects.all()
  serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveAPIView):
  """
  API endpoint for retrieving a single course by ID.
  """
  queryset = Course.objects.all()
  serializer_class = NestedCourseSerializer


class BriefCourseListView(generics.RetrieveAPIView):
  """
  API endpoint for retrieving a list of courses with brief information (excluding nested data).
  """
  queryset = Course.objects.all()
  serializer_class = CourseSerializer


  def get_queryset(self):
    queryset = super().get_queryset()
    # Filter courses to only include specific fields for brief information
    return queryset.values('id', 'bid', 'title', 'img', 'format', 'price')


# GET /api/courses: Retrieves a list of all courses with full details.
# GET /api/courses/<course_id>: Retrieves a single course by ID with nested information (skills, mentors, etc.).
# GET /api/courses/brief: Retrieves a list of courses with brief information (id, title, image, format, price).