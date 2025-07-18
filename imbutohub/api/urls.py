from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MilkRecordViewSet
from .views import PaymentViewSet,UserViewSet



router = DefaultRouter()
router.register(r'payments', PaymentViewSet)
router.register(r'users', UserViewSet, basename='user')
router.register(r"milkrecords", MilkRecordViewSet, basename='milkrecords')
urlpatterns = [
    path('', include(router.urls)),

]    





