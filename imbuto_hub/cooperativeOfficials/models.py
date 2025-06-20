from django.db import models

# Create your models here.

class CooperativeOfficial(models.Model):
    official_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)  
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name
