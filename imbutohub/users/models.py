from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('farmer', 'Farmer'),
        ('cooperative_official', 'Cooperative Official'),
    )
    user_type = models.CharField(max_length=32, choices=USER_TYPE_CHOICES)
    member_id = models.CharField(max_length=128, blank=True, null=True)
    national_id = models.CharField(max_length=128, blank=True, null=True)
    gender = models.CharField(max_length=16, blank=True, null=True)
    phone_number = models.CharField(max_length=32, blank=True, null=True)
    full_name = models.CharField(max_length=256, blank=True, null=True)

    role = models.CharField(max_length=128, blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now, editable=False)


    groups = models.ManyToManyField(
        Group,
        related_name='custom_users', 
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='custom_user',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_users', 
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='custom_user',
    )

    def __str__(self):
        return self.username
