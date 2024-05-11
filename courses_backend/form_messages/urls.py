from django.urls import path
from .views import FormMessageListCreate, FormMessageRetrieveUpdateDestroy

urlpatterns = [
    path('form-messages/', FormMessageListCreate.as_view(), name='form-message-list'),
    path('form-messages/<int:pk>/', FormMessageRetrieveUpdateDestroy.as_view(), name='form-message-detail'),
]
