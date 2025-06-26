


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


















# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from .models import Payment
 

# class PaymentAPITests(APITestCase):

#     def setUp(self):
       
#         self.cooperative_official = CooperativeOfficial.objects.create(
#             full_name='Official Name',
#             username='official_username',
#             password='securepassword',
#             email='official@example.com',
#             role='Official'
#         )

#         self.farmer = Farmer.objects.create(
#             first_name='John',
#             last_name='Doe',
#             member_id='M123',
#             national_id='N123456789',
#             email='john.doe@example.com',
#             password='securepassword',
#             gender='Male',
#             phone_number='1234567890'
#         )
        
#         self.milk_record = MilkRecord.objects.create(
#             farmer_id=self.farmer,
#             quantity_ltrs=10.00,
#             price_per_ltr=5.00,
#             amount_to_pay=50.00,
#             date='2023-10-01',
#             official_id=self.cooperative_official  
#         )

#         self.payment = Payment.objects.create(
#             payment_status='Pending',
#             price_per_ltr=10.00,
#             total_amount=100.00,
#             farmer_id=self.farmer,
#             payment_date='2023-10-01'
#         )
#         self.payment.records_id.add(self.milk_record)

#     def test_get_payment(self):
#         response = self.client.get(reverse('payment-detail', args=[self.payment.payment_id]))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_create_payment(self):
#         data = {
#             'payment_status': 'Paid',
#             'price_per_ltr': 15.00,
#             'total_amount': 150.00,
#             'farmer_id': self.farmer.farmer_id,  
#             'payment_date': '2023-10-02', 
#             'records_id': [self.milk_record.id] 
#         }
#         response = self.client.post(reverse('payment-list'), data, format='json')
#         print(response.data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_update_payment(self):
#         data = {
#             'payment_status': 'Paid',
#             'price_per_ltr': 12.00,
#             'total_amount': 120.00
#         }
#         response = self.client.patch(reverse('payment-detail', args=[self.payment.payment_id]), data, format='json')
#         print(response.data)  
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_delete_payment(self):
#         response = self.client.delete(reverse('payment-detail', args=[self.payment.payment_id]))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)