from django.shortcuts import render
from Payments.models import Payment
from .serializer import PaymentsSerializer

# Create your views here.
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentsSerializer
    