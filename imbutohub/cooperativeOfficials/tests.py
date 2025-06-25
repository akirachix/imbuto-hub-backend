from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import CooperativeOfficial

class CooperativeOfficialModelTest(TestCase):
    def setUp(self):
        self.official = CooperativeOfficial.objects.create(
            full_name="Jane Doe",
            username="janedoe",
            password="supersecretpassword", 
            email="jane@example.com",
            role="Chairperson"
        )

    def test_cooperative_official_str(self):
        """Test the __str__ method returns the full name."""
        self.assertEqual(str(self.official), "Jane Doe")

    def test_official_fields(self):
        """Test the fields are correctly assigned."""
        self.assertEqual(self.official.full_name, "Jane Doe")
        self.assertEqual(self.official.username, "janedoe")
        self.assertEqual(self.official.email, "jane@example.com")
        self.assertEqual(self.official.role, "Chairperson")
        self.assertIsNotNone(self.official.created_at)
        self.assertIsInstance(self.official.official_id, int)

    def test_unique_username(self):
        """Test that creating a duplicate username raises an error."""
        with self.assertRaises(Exception):
            CooperativeOfficial.objects.create(
                full_name="John Smith",
                username="janedoe",  
                password="anotherpassword",
                email="johnsmith@example.com",
                role="Treasurer"
            )

    def test_unique_email(self):
        """Test that creating a duplicate email raises an error."""
        with self.assertRaises(Exception):
            CooperativeOfficial.objects.create(
                full_name="John Smith",
                username="johnsmith",
                password="anotherpassword",
                email="jane@example.com",  
                role="Treasurer"
            )