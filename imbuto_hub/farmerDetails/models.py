from django.db import models
class Farmer(models.Model):
    farmer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    member_id = models.CharField(max_length=100)  
    national_id = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128) 
    gender = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Create your models here.
