from django.test import TestCase
from .models import User

class UserModelTest(TestCase):

    def setUp(self):
        self.farmer = User.objects.create(
            user_type="farmer",
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            username="johnny",
            password="testpassword123",
            member_id="F123",
            national_id="123456789",
            gender="male",
            phone_number="0712345678"
        )
        self.official = User.objects.create(
            user_type="cooperative_official",
            first_name="Jane",
            last_name="Smith",
            email="jane.smith@example.com",
            username="jsmith",
            password="testpassword123",
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
                first_name="Dup",
                last_name="Email",
                email="john.doe@example.com",  
                username="dupemail",
                password="testpassword123"
            )

    def test_username_unique(self):
        with self.assertRaises(Exception):
            User.objects.create(
                user_type="farmer",
                first_name="Dup",
                last_name="Username",
                email="dupuser@example.com",
                username="johnny",  # duplicate
                password="testpassword123"
            )

    def test_gender_choices(self):
        user = User.objects.create(
            user_type="farmer",
            first_name="Sam",
            last_name="Smith",
            email="sam.smith@example.com",
            username="samsmith",
            password="testpassword123",
            gender="other"
        )
        self.assertEqual(user.gender, "other")

    def test_created_at_field(self):
        self.assertIsNotNone(self.farmer.created_at)
        self.assertIsNotNone(self.official.created_at)