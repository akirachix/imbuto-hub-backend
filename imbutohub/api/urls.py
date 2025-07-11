from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MilkRecordViewSet




router = DefaultRouter()
router.register(r"milkrecords", MilkRecordViewSet, basename='milkrecords')

urlpatterns = [
    path('', include(router.urls)),
]    
from users.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
