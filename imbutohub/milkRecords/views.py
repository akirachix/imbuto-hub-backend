from django.shortcuts import render

from milkRecords.models import MilkRecord
from .serializer import  MilkRecordSerializer

# Create your views here.
class MilkRecordViewSet(viewsets.ModelViewSet):
    queryset = MilkRecord.objects.all()
    serializer_class = MilkRecordSerializer