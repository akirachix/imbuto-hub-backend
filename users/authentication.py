from django.contrib.auth.backends import BaseBackend
from users.models import User
class PhoneNumberPasswordBackend(BaseBackend):
    def authenticate(self, request, member_id=None, password=None, **kwargs):
        try:
            user = User.objects.get(member_id=member_id)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
