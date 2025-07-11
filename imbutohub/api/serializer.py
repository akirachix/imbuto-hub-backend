from rest_framework import serializers

from Payments.models import Payment


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

