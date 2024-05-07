
from rest_framework import viewsets
from .models import PaymentOperation
from .serializers import PaymentOperationSerializer


class PaymentOperationViewSet(viewsets.ModelViewSet):
    queryset = PaymentOperation.objects.all()
    serializer_class = PaymentOperationSerializer
