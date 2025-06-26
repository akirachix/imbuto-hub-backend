from django.db import models

# Create your models here.
from django.core.validators import RegexValidator
from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('farmer', 'Farmer'),
        ('official', 'Cooperative Official'),
    ]
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('', 'Not Specified'),
    ]

    user_id = models.AutoField(primary_key=True)
    # Common fields
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    # Farmer-specific fields (can be blank for officials)
    member_id = models.CharField(max_length=100, blank=True, null=True)
    national_id = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True, null=True)
    phone_number = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message='Phone number must be exactly 10 digits.',
                code='invalid_phone_number'
            ),
        ]
    )

    def __str__(self):
        return self.full_name