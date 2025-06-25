from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from FarmerDetails.models import Farmer

class FarmerAPITests(APITestCase):
    def setUp(self):
        self.farmer_data = {
            "name": "John Doe",
            "age": 30,
            "location": "Nairobi",
            # add all required fields for Farmer model here
        }
        self.farmer = Farmer.objects.create(**self.farmer_data)
        self.list_url = reverse('farmers-list')

    def test_list_farmers(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_farmer(self):
        data = {
            "name": "Jane Smith",
            "age": 28,
            "location": "Kisumu",
            # add all required fields for Farmer model here
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Farmer.objects.count(), 2)

    def test_retrieve_farmer(self):
        url = reverse('farmers-detail', args=[self.farmer.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.farmer_data['name'])

    def test_update_farmer(self):
        url = reverse('farmers-detail', args=[self.farmer.id])
        update_data = self.farmer_data.copy()
        update_data['name'] = "Updated Farmer"
        response = self.client.put(url, update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.farmer.refresh_from_db()
        self.assertEqual(self.farmer.name, "Updated Farmer")

    def test_delete_farmer(self):
        url = reverse('farmers-detail', args=[self.farmer.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Farmer.objects.filter(id=self.farmer.id).exists())