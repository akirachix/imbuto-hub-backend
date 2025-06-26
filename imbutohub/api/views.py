from django.shortcuts import render
from Payments.models import Payment
from .serializer import PaymentsSerializer
from rest_framework import viewsets

# Create your views here.
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentsSerializer
    