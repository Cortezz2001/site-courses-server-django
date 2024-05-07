from django.urls import path
from . import views

urlpatterns = [
    path('coaches/', views.MentorListView.as_view(), name='mentor-list'),
    path('coaches/<int:pk>/', views.MentorDetailView.as_view(), name='mentor-detail'),
    path('coaches/brief/', views.BriefMentorListView.as_view(), name='mentor-brief-list'),
]