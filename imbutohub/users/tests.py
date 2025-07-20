from django.test import TestCase
from users.models import User

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', password='pass')
        self.assertEqual(user.username, 'testuser')