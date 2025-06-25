from django.shortcuts import render
from rest_framework import viewsets


from milkRecords.models import MilkRecord
from .serializer import  MilkRecordSerializer



class MilkRecordViewSet(viewsets.ModelViewSet):
    queryset = MilkRecord.objects.all()
    serializer_class = MilkRecordSerializer