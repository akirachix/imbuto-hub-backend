from django.shortcuts import render
from Payments.models import Payment
from .serializer import PaymentsSerializer
from rest_framework import viewsets



# Create your views here.
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentsSerializer
    

















class MilkRecordViewSet(viewsets.ModelViewSet):
    queryset = MilkRecord.objects.all()
    serializer_class = MilkRecordSerializer
from django.http import HttpResponse

def api_home(request):
    return HttpResponse("API Home")

def example_view(request):
    return HttpResponse("Example API View")

