
from django.urls import path
from .views import user_registration, check_user_authentification, user_authentification, user_logout, get_token_csrf

urlpatterns = [
    path('user_registration', user_registration),
    path('check_user_authentification', check_user_authentification),
    path('user_authentification', user_authentification),
    path('user_logout', user_logout),
    path('get_csrf_token', get_token_csrf),
]
