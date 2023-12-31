from django.contrib.auth.base_user import BaseUserManager
from .utils import create_activation_code


class MyUserManager(BaseUserManager):
    """custom UserManager"""
    use_in_migrations = True

    def create_user(self, email, password, **extra_fields):
        # username =
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        create_activation_code(instance=user)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user