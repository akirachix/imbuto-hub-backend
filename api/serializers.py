from rest_framework import serializers
from users.models import User 
from  Payments.models import Payment
from milkRecords.models import MilkRecord

from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'




class MilkRecordSerializer(serializers.ModelSerializer):
    member_identifier = serializers.CharField(source='member_id.member_id', read_only=True)
    first_name = serializers.CharField(source='member_id.first_name', read_only=True)
    last_name = serializers.CharField(source='member_id.last_name', read_only=True)
    phone_number = serializers.CharField(source='member_id.phone_number', read_only=True)

    class Meta:
        model = MilkRecord
        fields = ['record_id', 'member_id', 'member_identifier', 'first_name', 'last_name', 'phone_number', 'quantity', 'amount_to_pay', 'date']

       
class PaymentSerializer(serializers.ModelSerializer):
    member_identifier = serializers.CharField(source='member_id.member_id', read_only=True)
    first_name = serializers.CharField(source='member_id.first_name', read_only=True)
    last_name = serializers.CharField(source='member_id.last_name', read_only=True)

    class Meta:
        model = Payment
        fields = [ 'payment_status', 'total_amount', 'member_id', 'member_identifier', 'first_name', 'last_name', 'payment_date', 'records_id']




class LoginSerializer(serializers.Serializer):
    member_id = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(member_id=data['member_id'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        return user






class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, max_length=128)
    member_id = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['user_type', 'phone_number', 'first_name', 'last_name', 'member_id', 'password', 'national_id']
        extra_kwargs = {
            'user_type': {'required': True},
        }

    def validate_user_type(self, value):
        allowed_user_types = ['farmer', 'cooperative_official']
        if value not in allowed_user_types:
            raise serializers.ValidationError("User type must be either 'farmer' or 'cooperative_official'.")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        member_id = validated_data.pop('member_id')  
        user = User.objects.create_user(member_id=member_id, password=password, **validated_data)
        return user










from rest_framework import serializers
class STKPushSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    account_reference = serializers.CharField()
    transaction_desc = serializers.CharField()