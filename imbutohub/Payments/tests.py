# from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Payment
from FarmerDetails.models import Farmer  # Adjust the import based on your app structure
from milkRecords.models import MilkRecord  # Adjust the import based on your app structure


class PaymentAPITests(APITestCase):

    def setUp(self):
        # Create a farmer instance
        self.farmer = Farmer.objects.create(
            first_name='John',
            last_name='Doe',
            member_id='M123',
            national_id='N123456789',
            email='john.doe@example.com',
            password='securepassword',
            gender='Male',
            phone_number='1234567890'
        )
        
        # Create a milk record instance
        self.milk_record = MilkRecord.objects.create(
            farmer_id=self.farmer,
            quantity_ltrs=10.00,
            price_per_ltr=5.00,
            amount_to_pay=50.00,
            date='2023-10-01',
            official_id='Official123'  # Use a valid official ID
        )

        # Create a payment instance
        self.payment = Payment.objects.create(
            payment_status='Pending',
            price_per_ltr=10.00,
            total_amount=100.00,
            farmer_id=self.farmer,
            payment_date='2023-10-01'
        )
        self.payment.records_id.add(self.milk_record)

    def test_get_payment(self):
        response = self.client.get(reverse('payment-detail', args=[self.payment.payment_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_payment(self):
        data = {
            'payment_status': 'Paid',
            'price_per_ltr': 15.00,
            'total_amount': 150.00,
            'farmer_id': self.farmer.farmer_id,  # Use farmer_id if that is your PK field
            'payment_date': '2023-10-02',
            'records_id': [self.milk_record.record_id]  # Use record_id if that is your PK field
        }
        response = self.client.post(reverse('payment-list'), data, format='json')
        print(response.data)  # For debugging
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_payment(self):
        # Use PATCH for partial update to avoid sending all required fields
        data = {
            'payment_status': 'Paid',
            'price_per_ltr': 12.00,
            'total_amount': 120.00
        }
        response = self.client.patch(reverse('payment-detail', args=[self.payment.payment_id]), data, format='json')
        print(response.data)  # For debugging
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_payment(self):
        response = self.client.delete(reverse('payment-detail', args=[self.payment.payment_id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)