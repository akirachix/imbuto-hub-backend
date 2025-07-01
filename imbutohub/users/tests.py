from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User

class UserEndpointTest(APITestCase):
    def setUp(self):
        self.url = reverse('user-list') 

    def test_create_farmer(self):
        data = {
            "user_type": "farmer",
            "first_name": "John",
            "last_name": "Doe",
            "member_id": "M123",
            "national_id": "NID12345",
            "email": "johnfarmer@example.com",
            "password": "password123",
            "gender": "male",
            "phone_number": "1234567890"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().user_type, "farmer")

    def test_create_cooperative_official(self):
        data = {
            "user_type": "cooperative_official",
            "full_name": "Jane Admin",
            "username": "adminjane",
            "email": "janeofficial@example.com",
            "password": "password456",
            "role": "Admin"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().user_type, "cooperative_official")

    def test_list_users(self):
        User.objects.create(user_type="farmer", first_name="John", last_name="Kiptoo", email="chepchep@kiptoo.com", password="kiptoo123", member_id="001", national_id="kiptooid", gender="m", phone_number="111")
        User.objects.create(user_type="cooperative_official", full_name="Peter Kamande", username="peterkamande", email="peter@kamande.com", password="peter123", role="manager")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_by_user_type(self):
        User.objects.create(user_type="farmer", first_name="John", last_name="Kiptoo", email="chepchep@kiptoo.com", password="kiptoo123", member_id="001", national_id="kiptooid", gender="m", phone_number="111")
        User.objects.create(
    user_type="cooperative_official",
    first_name="Peter",
    last_name="Kamande",
    username="peterkamande",
    email="peter@kamande.com",
    password="peter123"
)
        response = self.client.get(self.url + '?user_type=farmer')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['user_type'], 'farmer')

        