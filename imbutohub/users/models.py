from django.db import models


class User(models.Model):
    GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
    ('prefer_not_to_say', 'Prefer not to say'),
]


    USER_TYPE_CHOICES = [
        ('farmer', 'Farmer'),
        ('cooperative_official', 'Cooperative Official'),
    ]
    user_type = models.CharField(max_length=32, choices=USER_TYPE_CHOICES)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True, null=True, blank=True)




    password = models.CharField(max_length=128)

    
    member_id = models.CharField(max_length=100, null=True, blank=True)
    national_id = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=17, choices=GENDER_CHOICES, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        if self.user_type == 'farmer':
            return f"{self.first_name or ''} {self.last_name or ''}".strip()
        return self.username or self.email