
from django.db import models
from users.models import User
# Create your models here.
class MilkRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    farmer_id= models.ForeignKey(User, on_delete=models.CASCADE, related_name='milk_records')
    quantity_ltrs = models.DecimalField(max_digits=5, decimal_places=2)
    price_per_ltr = models.DecimalField(max_digits=10, decimal_places=2)
    amount_to_pay = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    official_id = models.CharField(User,max_length=100)  # Optional: use FK if coop table exists
    def __str__(self):
        return f"MilkRecord {self.record_id} - {self.farmer.first_name}"






