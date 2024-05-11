from django.urls import path
from .views import FormMessageListCreate, FormMessageRetrieveUpdateDestroy

urlpatterns = [
    path('', FormMessageListCreate.as_view(), name='form-message-list'),
    path('<int:pk>/', FormMessageRetrieveUpdateDestroy.as_view(), name='form-message-detail'),
]
