from rest_framework import serializers
from users.models import User 
from  Payments.models import Payment
from milkRecords.models import MilkRecord

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "member_id", "first_name", "last_name", "user_type", "email",
            "password", "national_id", "gender", "phone_number", "username"
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate(self, attrs):
        print("Custom validation running!")  
        user_type = attrs.get('user_type')
        errors = {}

        farmer_fields = ['first_name', 'last_name', 'national_id', 'gender', 'phone_number']
        official_fields = ['first_name', 'last_name', 'username']

        if user_type == 'farmer':
            for field in farmer_fields:
                if not attrs.get(field):
                    errors[field] = 'This field is required for farmers.'
        elif user_type == 'cooperative_official':
            for field in official_fields:
                if not attrs.get(field):
                    errors[field] = 'This field is required for cooperative officials.'
        else:
            errors['user_type'] = "Invalid user_type. Must be 'farmer' or 'cooperative_official'."

        if errors:
            raise serializers.ValidationError(errors)
        return attrs
        
        if User.objects.filter(member_id=value).exists():
            raise serializers.ValidationError("A user with member_id already exists.")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

from milkRecords.models import MilkRecord
class MilkRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilkRecord
        fields = '__all__'

from rest_framework import serializers


class PaymentSerializer(serializers.ModelSerializer):
  class Meta:
      model = Payment
      fields = "__all__"



# class STKPushSerializer(serializers.Serializer):
#     phone_number = serializers.CharField()
#     amount = serializers.DecimalField(max_digits=10, decimal_places=2)
#     account_reference = serializers.CharField()
#     transaction_desc = serializers.CharField()




from rest_framework import serializers
class STKPushSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    account_reference = serializers.CharField()
    transaction_desc = serializers.CharField()