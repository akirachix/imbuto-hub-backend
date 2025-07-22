


from django.test import TestCase
from .models import Payment
from datetime import date

class PaymentModelTest(TestCase):
    def setUp(self):
        self.payment = Payment.objects.create(
            payment_status='Pending',
            price_per_ltr=42.50,
            total_amount=100.00,
            payment_date=date(2025, 6, 26)
        )

    def test_payment_creation(self):
        self.assertEqual(self.payment.payment_status, 'Pending')
        self.assertEqual(float(self.payment.price_per_ltr), 42.50)
        self.assertEqual(float(self.payment.total_amount), 100.00)
        self.assertEqual(self.payment.payment_date, date(2025, 6, 26))


















