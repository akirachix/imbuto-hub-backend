from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CooperativeOfficialViewSet

router = DefaultRouter()
router.register(r'cooperative-officials', CooperativeOfficialViewSet)

urlpatterns = router.urls