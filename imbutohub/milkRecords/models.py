
from django.db import models
from users.models import User


class MilkRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    member_id= models.ForeignKey(User, on_delete=models.CASCADE, related_name='milk_records')
    quantity_ltrs = models.DecimalField(max_digits=5, decimal_places=2)
    price_per_ltr = models.DecimalField(max_digits=10, decimal_places=2)
    amount_to_pay = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    def __str__(self):
        return f"MilkRecord {self.record_id} - {self.member_id.first_name}"





