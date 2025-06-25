from rest_framework import serializers
from FarmerDetails.models import Farmer
class FarmerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'