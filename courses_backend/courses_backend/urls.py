from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/mentors/', include("mentors.urls")),
    path('api/v1/courses/', include("courses.urls")),
    path('api/v1/auth/', include('auth_system.urls')),
    path('admin/', admin.site.urls),
]
