from rest_framework import serializers
from users.models import User  

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id", "first_name", "last_name", "user_type", "email",
            "password", "member_id", "national_id", "gender", "phone_number",
            "full_name", "role", "username"
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate(self, attrs):
        print("Custom validation running!")  
        user_type = attrs.get('user_type')
        errors = {}

        farmer_fields = ['first_name', 'last_name', 'member_id', 'national_id', 'gender', 'phone_number']
        official_fields = ['first_name','last_name', 'username']

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