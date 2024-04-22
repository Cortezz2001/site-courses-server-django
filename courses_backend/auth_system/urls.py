
from django.urls import path
from .views import user_registration, check_user_authentification, user_authentification

urlpatterns = [
    path('user_registration', user_registration),
    path('check_user_authentification', check_user_authentification),
    path('user_authentification', user_authentification),
]
