from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MilkRecordViewSet
from .views import PaymentViewSet,UserViewSet
from .views import STKPushView, daraja_callback

from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet, STKPushView, daraja_callback



from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import  OrderViewSet, STKPushView, daraja_callback




router =DefaultRouter()


router.register(r"payments", PaymentViewSet, basename="payments")
# router.register(r"orders", OrderViewSet, basename="orders")




urlpatterns = [
   path("", include(router.urls)),
   path('api/daraja/stk-push/', STKPushView.as_view(), name='daraja-stk-push'),
   path('daraja/callback/', daraja_callback, name='daraja-callback'),
   path('stkpush/', STKPushView.as_view(), name='stkpush'),
   path('daraja/callback/', daraja_callback, name='daraja_callback'),
]




router = DefaultRouter()
router.register(r'payments', PaymentViewSet)
router.register(r'users', UserViewSet, basename='user')
router.register(r"milkrecords", MilkRecordViewSet, basename='milkrecords')
urlpatterns = [
    path('', include(router.urls)),
    

]    

