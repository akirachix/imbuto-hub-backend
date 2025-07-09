from rest_framework import viewsets
from users.models import User
from .serializers import UserSerializer

class ImbutoHubViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
