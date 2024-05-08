from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer, NestedCourseSerializer


class CourseListView(generics.ListAPIView):
  """
  API endpoint for retrieving a list of all courses.
  """
  queryset = Course.objects.all()
  serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveAPIView):
  """
  API endpoint for retrieving a single course by ID with all related data.
  """
  queryset = Course.objects.all()
  serializer_class = NestedCourseSerializer
  lookup_field = 'pk'  # Use primary key for lookup

  def get_queryset(self):
    # Optional filtering based on URL parameters or other criteria
    return super().get_queryset()


# GET /api/courses: Retrieves a list of all courses with full details.
# GET /api/courses/<course_id>: Retrieves a single course by ID with nested information (skills, mentors, etc.).
# GET /api/courses/brief: Retrieves a list of courses with brief information (id, title, image, format, price).