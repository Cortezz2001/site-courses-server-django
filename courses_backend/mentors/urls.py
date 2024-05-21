from django.urls import path
from . import views

urlpatterns = [
    path('', views.MentorListView.as_view(), name='mentor-list'),
    path('<int:pk>/', views.MentorDetailView.as_view(), name='mentor-detail'),
]