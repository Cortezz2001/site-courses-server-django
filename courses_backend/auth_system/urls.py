
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import CheckAuth, Logout

urlpatterns = [
    path('', include("djoser.urls")),
    path('checkAuth', CheckAuth.as_view()),
    path('logout', Logout.as_view()),
    path('token', obtain_auth_token, name="token"),
]
