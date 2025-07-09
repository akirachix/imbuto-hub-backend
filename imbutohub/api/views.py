from django.shortcuts import render
from Payments.models import Payment
from .serializer import PaymentsSerializer
from rest_framework import viewsets



# Create your views here.
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentsSerializer
    

# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import viewsets
# from Payments.models import Payment
# from .serializer import PaymentsSerializer
# # :brain: MTN MoMo logic import
# from Payments.services.momo import disburse_money_to_farmer
# # :white_check_mark: Leave out Farmer & MilkRecord for now
# # from Payments.models import Farmer, MilkRecord
# # Internal Payment API ViewSet (unchanged)
# class PaymentViewSet(viewsets.ModelViewSet):
#     queryset = Payment.objects.all()
#     serializer_class = PaymentsSerializer
# # :moneybag: MoMo Disbursement Endpoint using mock data
# class DisburseToFarmers(APIView):
#     def post(self, request):
#         # Temporary hardcoded farmer data
#         farmers = [
#             {
#                 "member_id": "F001",
#                 "phone_number": "250712345678",  # Replace with a valid MoMo sandbox MSISDN
#                 "amount": 1000,
#             },
#             {
#                 "member_id": "F002",
#                 "phone_number": "250798765432",  # Replace with a valid MoMo sandbox MSISDN
#                 "amount": 1200,
#             },
#         ]
#         results = []
#         for farmer in farmers:
#             result = disburse_money_to_farmer(
#                 amount=farmer["amount"],
#                 farmer_mobile=farmer["phone_number"],
#                 external_id=farmer["member_id"],
#                 reason="Milk payment for last 15 days",
#             )
#             result["farmer"] = farmer["member_id"]
#             result["amount"] = farmer["amount"]
#             results.append(result)
#         return Response(results)

















