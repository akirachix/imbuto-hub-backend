from django.shortcuts import render
from rest_framework import viewsets


from milkRecords.models import MilkRecord
from .serializer import  MilkRecordSerializer



class MilkRecordViewSet(viewsets.ModelViewSet):
    queryset = MilkRecord.objects.all()
    serializer_class = MilkRecordSerializer
from django.http import HttpResponse

def api_home(request):
    return HttpResponse("API Home")

def example_view(request):
    return HttpResponse("Example API View")
