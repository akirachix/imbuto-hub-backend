from rest_framework import serializers
from django.contrib.auth.models import User 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
def validate(self, users):
        print("Validation in progress")  
        user_type = users.get('user_type')
        errors = {}
        

        farmer_fields = ['first_name', 'last_name', 'member_id', 'national_id', 'gender', 'phone_number']
        official_fields = ['first_name','last_name', 'username']

        if user_type == 'farmer':
            for field in farmer_fields:
                if not users.get(field):
                    errors[field] = 'This field is required for farmers.'
        elif user_type == 'cooperative_official':
            for field in official_fields:
                if not users.get(field):
                    errors[field] = 'This field is required for cooperative officials.'
        else:
            errors['user_type'] = "Invalid user_type. Must be 'farmer' or 'cooperative_official'."

        if errors:
            raise serializers.ValidationError(errors)
        return users
