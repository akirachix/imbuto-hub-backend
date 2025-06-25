from django.shortcuts import render
from rest_framework import viewsets
from FarmerDetails.models import Farmer
from .serializer import FarmerDetailsSerializer
class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerDetailsSerializer