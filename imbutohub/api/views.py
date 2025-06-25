from django.shortcuts import render
from rest_framework import viewsets

from Payments.models import Payment
from .serializer import PaymentsSerializer



class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentsSerializer