from rest_framework import serializers
from cooperativeOfficials.models import CooperativeOfficial

class CooperativeOfficialSerializer(serializers.ModelSerializer):
    class Meta:
        model = CooperativeOfficial
        fields = '__all__'

        