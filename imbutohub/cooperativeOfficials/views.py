from django.shortcuts import render
from rest_framework import viewsets
from FarmerDetails.models import Farmer
from cooperativeOfficials.models import CooperativeOfficial
from .serializers import FarmerDetailsSerializer, CooperativeOfficialSerializer


class CooperativeOfficialViewSet(viewsets.ModelViewSet):
    queryset = CooperativeOfficial.objects.all()
    serializer_class = CooperativeOfficialSerializer