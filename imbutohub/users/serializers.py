from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate(self, attrs):
        print("Custom validation running!")  # Add this line
        user_type = attrs.get('user_type')
        errors = {}
        

        farmer_fields = ['first_name', 'last_name', 'member_id', 'national_id', 'gender', 'phone_number']
        official_fields = ['full_name', 'username', 'role']

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