from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentOperationViewSet

router = DefaultRouter()
router.register('payments', PaymentOperationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]