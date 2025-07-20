from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group, Permission

from django.db.models import Max
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('farmer', 'Farmer'),
        ('cooperative_official', 'Cooperative Official'),
    )
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    user_type = models.CharField(max_length=32, choices=USER_TYPE_CHOICES)
    member_id = models.CharField(max_length=128, blank=True, null=True, unique=True, editable=False)
    national_id = models.CharField(max_length=128, blank=True, null=True)
    gender = models.CharField(max_length=16, choices=GENDER_CHOICES, blank=True, null=True)
    phone_number = models.CharField(max_length=32, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
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
    def save(self, *args, **kwargs):

        if not self.member_id:
            prefix = 'F' if self.user_type == 'farmer' else 'C'

            max_member = User.objects.filter(user_type=self.user_type, member_id__startswith=prefix).aggregate(
                max_num = Max(models.functions.Cast(models.Substr('member_id',2), models.IntegerField()))
            )['max_num']

            next_num = (max_member or 0) + 1
            self.member_id = f"{prefix}{next_num:03d}"

        super(User, self).save(*args, **kwargs)
            
















