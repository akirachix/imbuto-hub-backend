from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from Payments.models import Payment  # your Payment model (adjust import if needed)
from users.models import User  # your custom User model
from .serializers import STKPushSerializer  # your serializer for STK push input
from some_module import DarajaAPI  # import your Daraja API interface
import datetime
from django.utils import timezone
class STKPushView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
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
            checkout_request_id = response.get('CheckoutRequestID')
            # Attach user if authenticated
            user = None
            if request.user.is_authenticated:
                try:
                    user = User.objects.get(id=request.user.id)
                except User.DoesNotExist:
                    user = None
            if checkout_request_id:
                payment = Payment.objects.create(
                    phone_number=data['phone_number'],
                    amount=data['amount'],
                    account_reference=data['account_reference'],
                    transaction_desc=data['transaction_desc'],
                    mpesa_checkout_id=checkout_request_id,
                    quantity=1,
                    type='payment',
                    condition='New',
                    price=data['amount'],
                )
                if user:
                    # Adjust depending on your Payment model's fields to link user
                    payment.user = user
                    payment.save()
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.decorators import api_view
@api_view(['POST'])
def daraja_callback(request):
    callback_data = request.data
    print("Daraja Callback Data:", callback_data)
    try:
        stk_callback = callback_data['Body']['stkCallback']
        checkout_request_id = stk_callback['CheckoutRequestID']
        result_code = stk_callback['ResultCode']
        result_desc = stk_callback['ResultDesc']
        payment = Payment.objects.get(mpesa_checkout_id=checkout_request_id)
        payment.result_code = str(result_code)
        payment.result_description = result_desc
        if result_code == 0:
            items = stk_callback.get('CallbackMetadata', {}).get('Item', [])
            item_dict = {item['Name']: item['Value'] for item in items}
            payment.mpesa_receipt_number = item_dict.get('MpesaReceiptNumber')
            trans_date_str = str(item_dict.get('TransactionDate'))
            if trans_date_str:
                trans_date = datetime.datetime.strptime(trans_date_str, '%Y%m%d%H%M%S')
                payment.transaction_date = timezone.make_aware(trans_date, timezone.get_current_timezone())
            payment.amount_from_callback = item_dict.get('Amount')
            payment.phone_number_from_callback = item_dict.get('PhoneNumber')
            payment.payment_status = 'Completed'
        else:
            payment.payment_status = 'Failed'
        payment.save()
    except Payment.DoesNotExist:
        print(f"Payment with CheckoutRequestID {checkout_request_id} not found.")
    except Exception as e:
        print(f"Error processing Daraja callback: {e}")
    return Response({"ResultCode": 0, "ResultDesc": "Accepted"}, status=status.HTTP_200_OK)