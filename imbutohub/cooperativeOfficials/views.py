from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework import viewsets
from FarmerDetails.models import Farmer
from cooperativeOfficials.models import CooperativeOfficial
from .serializer import FarmerDetailsSerializer, CooperativeOfficialSerializer
class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerDetailsSerializer

class CooperativeOfficialViewSet(viewsets.ModelViewSet):
    queryset = CooperativeOfficial.objects.all()
    serializer_class = CooperativeOfficialSerializer



