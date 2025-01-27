from django.contrib.auth.backends import BaseBackend
from .models import ClientUser


class ClientUserBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = ClientUser.objects.get(email=email)
            if user.check_password(password):
                return user
        except ClientUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return ClientUser.objects.get(pk=user_id)
        except ClientUser.DoesNotExist:
            return None
