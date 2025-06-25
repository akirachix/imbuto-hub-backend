from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Farmer

class FarmerAPITestCase(APITestCase):
    def setUp(self):
        self.farmer = Farmer.objects.create(
            first_name="John",
            last_name="Doe",
            member_id="MBR001",
            national_id="123456789",
            email="john@example.com",
            password="testpassword123",
            gender="Male",
            phone_number="0712345678"
        )
        self.valid_payload = {
            "first_name": "Alice",
            "last_name": "Smith",
            "member_id": "MBR002",
            "national_id": "987654321",
            "email": "alice@example.com",
            "password": "securepassword",
            "gender": "Female",
            "phone_number": "0799999999"
        }

    def test_create_farmer(self):
        url = reverse('farmers-list')
        response = self.client.post(url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Farmer.objects.count(), 2)
        self.assertEqual(Farmer.objects.last().email, "alice@example.com")

    def test_get_farmer_list(self):
        url = reverse('farmers-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # If paginated, check 'results', else check response data
        if isinstance(response.data, dict) and "results" in response.data:
            self.assertIsInstance(response.data["results"], list)
        else:
            self.assertIsInstance(response.data, list)

    def test_get_single_farmer(self):
        url = reverse('farmers-detail', kwargs={'pk': self.farmer.farmer_id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.farmer.email)

    def test_update_farmer(self):
        url = reverse('farmers-detail', kwargs={'pk': self.farmer.farmer_id})
        updated_data = self.valid_payload.copy()
        updated_data["email"] = "updated@example.com"
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.farmer.refresh_from_db()
        self.assertEqual(self.farmer.email, "updated@example.com")

    def test_delete_farmer(self):
        url = reverse('farmers-detail', kwargs={'pk': self.farmer.farmer_id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Farmer.objects.filter(pk=self.farmer.farmer_id).exists())