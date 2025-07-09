from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from .views import ImbutoHubViewSet  # Your other API viewsets

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'imbutohub', ImbutoHubViewSet, basename='imbutohub')

urlpatterns = [
    path('', include(router.urls)),
]
