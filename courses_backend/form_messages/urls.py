from django.urls import path
from .views import FormMessageListCreate

urlpatterns = [
    path('', FormMessageListCreate.as_view(), name='form-message-list'),
]
