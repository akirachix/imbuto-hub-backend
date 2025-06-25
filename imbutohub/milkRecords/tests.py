from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from datetime import date
from FarmerDetails.models import Farmer
from cooperativeOfficials.models import CooperativeOfficial
from milkRecords.models import MilkRecord
# Create your tests here.


class MilkRecordAPITest(APITestCase):
    def setUp(self):
        # Create related Farmer and CooperativeOfficial
        self.farmer = Farmer.objects.create(



            first_name="Kebede",
            last_name="Abera",
            member_id="M1234",
            national_id="N987654321",
            email="kebedeabera@gmail.com",
            password="testpassword",
            gender="Male",
            phone_number="073456789"
        )
        self.official = CooperativeOfficial.objects.create(

        
             full_name="Tesfay Abrha",
             username="abrha",
             password="asdcpassword",
             email="tesfay@gmail.com",
             role="manager"
        )
        # Create sample MilkRecord
        self.milkrecord = MilkRecord.objects.create(
            farmer_id=self.farmer,
            quantity_ltrs=10.0,
            price_per_ltr=50.00,
            amount_to_pay=500.00,
            date=date.today(),
            official_id=self.official,
        )
        self.url = reverse('milkrecords-list')

    def test_list_milkrecords(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_milkrecord(self):
        data = {
            "farmer_id": self.farmer.id,
            "quantity_ltrs": "12.5",
            "price_per_ltr": "45.00",
            "amount_to_pay": "562.50",
            "date": str(date.today()),
            "official_id": self.official.id
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(float(response.data["quantity_ltrs"]), 12.5)

    def test_retrieve_milkrecord(self):
        url = reverse('milkrecords-detail', args=[self.milkrecord.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["record_id"], self.milkrecord.pk)

    def test_update_milkrecord(self):
        url = reverse('milkrecords-detail', args=[self.milkrecord.pk])
        data = {
            "farmer_id": self.farmer.farmer_id,
            "quantity_ltrs": "15.0",
            "price_per_ltr": "48.00",
            "amount_to_pay": "720.00",
            "date": str(date.today()),
            "official_id": self.official.official_id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(float(response.data["quantity_ltrs"]), 15.0)

    def test_delete_milkrecord(self):
        url = reverse('milkrecords-detail', args=[self.milkrecord.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(MilkRecord.objects.filter(pk=self.milkrecord.pk).exists())