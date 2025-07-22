from django.shortcuts import render
from Payments.models import Payment
from .serializers import PaymentsSerializer
from rest_framework import viewsets
from milkRecords.models import MilkRecord
from .serializers import  MilkRecordSerializer,UserSerializer

from users.models import User


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentsSerializer
    


class MilkRecordViewSet(viewsets.ModelViewSet):
    queryset = MilkRecord.objects.all()
    serializer_class = MilkRecordSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer






class MilkRecordViewSet(viewsets.ModelViewSet):
    queryset = MilkRecord.objects.all()
    serializer_class = MilkRecordSerializer
from django.http import HttpResponse

def api_home(request):
    return HttpResponse("API Home")

def example_view(request):
    return HttpResponse("Example API View")




from django.shortcuts import render
from rest_framework import viewsets


# from Payment.models import Payment
from .serializers import PaymentSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .daraja import DarajaAPI
from .serializers import STKPushSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response






class PaymentViewSet(viewsets.ModelViewSet):
  queryset=Payment.objects.all()
  serializer_class=PaymentSerializer


# class OrderViewSet(viewsets.ModelViewSet):
#   queryset = Order.objects.all()
#   serializer_class = OrderSerializer




from django.shortcuts import render
from rest_framework import viewsets


from Payments.models import Payment


# from .serializers import OrderSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .daraja import DarajaAPI
from .serializers import STKPushSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response




# class OrderViewSet(viewsets.ModelViewSet):
#    queryset = Order.objects.all()
#    serializer_class = OrderSerializer
class STKPushView(APIView):
  def post(self, request):
      serializer = STKPushSerializer(data=request.data)
      if serializer.is_valid():
          data = serializer.validated_data
          daraja = DarajaAPI()
          response = daraja.stk_push(
              phone_number=data['phone_number'],
              amount=data['amount'],
            #   order_item=data['order_item'],
              account_reference=data['account_reference'],
              transaction_desc=data['transaction_desc']
          )
          return Response(response)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








@api_view(['POST'])
def daraja_callback(request):
   print("Daraja Callback Data:", request.data)
   return Response({"ResultCode": 0, "ResultDesc": "Accepted"})

