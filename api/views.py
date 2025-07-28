from django.shortcuts import render
from Payments.models import Payment
from .serializers import PaymentSerializer
from rest_framework import viewsets
from milkRecords.models import MilkRecord
from .serializers import  MilkRecordSerializer,UserSerializer,RegisterSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .daraja import DarajaAPI
from .serializers import STKPushSerializer
from rest_framework.decorators import api_view
from users.models import User
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin
from users.permissions import IsFarmer
from users.permissions import IsCooperativeOfficial





class PaymentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    


class MilkRecordViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MilkRecord.objects.all()
    serializer_class = MilkRecordSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer



class MilkRecordViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MilkRecord.objects.all()
    serializer_class = MilkRecordSerializer
from django.http import HttpResponse

def api_home(request):
    return HttpResponse("API Home")

def example_view(request):
    return HttpResponse("Example API View")



class PaymentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer


class STKPushView(APIView):
  def post(self, request):
      serializer = STKPushSerializer(data=request.data)
      if serializer.is_valid():
          data = serializer.validated_data
          daraja = DarajaAPI()
          response = daraja.stk_push(
              phone_number=data['phone_number'],
              amount=data['amount'],
              account_reference=data['account_reference'],
              transaction_desc=data['transaction_desc']
          )
          return Response(response)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['POST'])
def daraja_callback(request):
   print("Daraja Callback Data:", request.data)
   return Response({"ResultCode": 0, "ResultDesc": "Accepted"})




class Login(APIView):
    def post (self,request):
        member_id = request.data.get('member_id')
        password= request.data.get('password')

        user = authenticate(request, member_id=member_id, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                                'token': token.key,
                                'usertype': user.user_type,
                                'member_id': user.member_id,
                                'first_name': user.first_name,
                                 })
        else:
            return Response({'error': 'Invalid member_id or password'}, status=status.HTTP_401_UNAUTHORIZED)





class RegisterView(APIView):
    permission_classes= [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'user_id': user.id,
                'member_id': user.member_id,
                'token': token.key,
                'user_type': user.user_type,
                'first_name': user.first_name,
                'last_name': user.last_name,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



