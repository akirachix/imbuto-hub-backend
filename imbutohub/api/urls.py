from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PaymentViewSet



router = DefaultRouter()
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import PaymentViewSet, DisburseToFarmers  # :white_check_mark: 1. Import the new view
# router = DefaultRouter()
# router.register(r'payments', PaymentViewSet)  # :white_check_mark: 2. Keep your existing router
# urlpatterns = [
#     path('', include(router.urls)),  # :white_check_mark: 3. Leave this as-is
#     path('disburse-farmers/', DisburseToFarmers.as_view(), name='disburse-farmers'),  # :white_check_mark: 4. Add this line
# ]