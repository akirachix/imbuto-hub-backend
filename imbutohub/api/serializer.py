


from rest_framework import serializers
from milkRecords.models import MilkRecord





class MilkRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilkRecord
        fields = '__all__'