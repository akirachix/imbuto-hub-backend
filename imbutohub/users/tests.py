from django.test import TestCase
from .models import User

class UserModelTest(TestCase):

    def setUp(self):
        self.farmer = User.objects.create(
            user_type="farmer",
            first_name="Mercy",
            last_name="King",
            email="mercy.king@example.com",
            username="mercy",
            password="password123",
            member_id="F123",
            national_id="123456789",
            gender="male",
            phone_number="0712345678"
        )
        self.official = User.objects.create(
            user_type="cooperative_official",
            first_name="joy",
            last_name="Wanjiku",
            email="joy.wanjiku@example.com",
            username="joywanji",
            password="password1723",
            member_id="O321",
            national_id="987654321",
            gender="female",
            phone_number="0798765432"
        )

    def test_farmer_str(self):
        self.assertEqual(str(self.farmer), "John Doe")

    def test_official_str(self):
        
        self.assertEqual(str(self.official), "jsmith")

    def test_email_unique(self):
        with self.assertRaises(Exception):
            User.objects.create(
            user_type="farmer",
            first_name="Mercy",
            last_name="King",
            email="mercy.king@example.com",
            username="mercy",
            password="password123"
            )

    def test_username_unique(self):
        with self.assertRaises(Exception):
            User.objects.create(
            user_type="cooperative_official",
            first_name="joy",
            last_name="Wanjiku",
            email="joy.wanjiku@example.com",
            username="joywanji",
            password="password1723"
            )

    def test_gender_choices(self):
        user = User.objects.create(
            user_type="farmer",
            first_name="Mercy",
            last_name="King",
            email="mercy.king@example.com",
            username="mercy",
            password="password123",
        )
        self.assertEqual(user.gender, "other")

    def test_created_at_field(self):
        self.assertIsNotNone(self.farmer.created_at)
        self.assertIsNotNone(self.official.created_at)