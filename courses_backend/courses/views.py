from django.shortcuts import render
from django.http import HttpRequest
from rest_framework import generics, viewsets

from .serializers import CourseSerializer
from .models import Course


def index(request):
    return HttpRequest("Hello world")


#class CoursesAPI(viewsets.ModelViewSet):
#    p = Course(course_name = "app", course_data="")
#    p.save()
#    print("create")
#    queryset = Course.objects.all()
#    serializer_class = CourseSerializer
