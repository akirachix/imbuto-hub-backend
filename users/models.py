from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, Group, PermissionsMixin,BaseUserManager
from django.db.models.functions import Substr
from django.db.models import IntegerField


class UserManager(BaseUserManager):
    def create_user(self, member_id, password=None, user_type="farmer", **extra_fields):
        if not member_id:
            raise ValueError("User must have a member id")
        if not password:
            raise ValueError("User must have a password")
        
        extra_fields.setdefault('user_type', user_type)  
        user = self.model(member_id=member_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, member_id, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('user_type', 'admin')  
        if not password:
            raise ValueError('Superuser must have a password')
        if not first_name:
            raise ValueError('Superuser must have a first name')
        if not last_name:
            raise ValueError('Superuser must have a last name')

        user = self.model(
            member_id=member_id,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user





from django.db.models import Max
class User(AbstractBaseUser,PermissionsMixin):

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
   
    def save(self, *args, **kwargs):

        if not self.member_id:
            prefix = 'F' if self.user_type == 'farmer' else 'C'

            max_member = User.objects.filter(user_type=self.user_type, member_id__startswith=prefix).aggregate(
    max_num=Max(
        models.functions.Cast(Substr('member_id', 2), IntegerField())
    )
)['max_num']

            next_num = (max_member or 0) + 1
            self.member_id = f"{prefix}{next_num:03d}"

        super(User, self).save(*args, **kwargs)



    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'member_id'
    REQUIRED_FIELDS = [  'first_name', 'last_name']


    class Meta:
            verbose_name = "user"
            verbose_name_plural = "users"
    
    def __str__(self):
        full_name = ' '.join(filter(None, [self.first_name, self.last_name]))
        if full_name.strip():
            return full_name
        if self.member_id:
            return self.member_id
        return "Unnamed User"




            
















