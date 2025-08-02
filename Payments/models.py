from django.db import models

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Paid', 'Paid')])
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    member_id = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='payments', default=1)  
    payment_date = models.DateField()
    records_id = models.ManyToManyField('milkRecords.MilkRecord', related_name='payments')

    def __str__(self):
        try:
            member_name = self.member_id.full_name or "Unknown Member"
        except AttributeError:
            member_name = "Unknown Member"
        return f"Payment {self.payment_id} - {member_name}"
