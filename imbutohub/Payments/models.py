from django.db import models

# Create your models here.

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Paid', 'Paid')])
    price_per_ltr = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    farmer_id = models.ForeignKey('FarmerDetails.Farmer', on_delete=models.CASCADE, related_name='payments')
    payment_date = models.DateField()
    records_id = models.ManyToManyField('milkRecords.MilkRecord', related_name='payments')


    def __str__(self):
        return f"Payment {self.payment_id} - {self.farmer_id.first_name}"
