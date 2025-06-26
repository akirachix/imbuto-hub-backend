from django.shortcuts import render
from rest_framework import viewsets
from cooperativeOfficials.models import CooperativeOfficial
from .serializers import CooperativeOfficialSerializer


class CooperativeOfficialViewSet(viewsets.ModelViewSet):
    queryset = CooperativeOfficial.objects.all()
    serializer_class = CooperativeOfficialSerializer