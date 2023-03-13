from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class UserModel(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shipping_address = models.CharField(verbose_name='Адрес доставки', max_length=254)
    phone_number = models.CharField( verbose_name='Номер телефона', max_length=254)
    email = models.EmailField(verbose_name='Почта', max_length=300, unique=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

# import uuid
# from datetime import timedelta
#
# from django.db import models
# from django.contrib.auth.models import AbstractUser, UserManager, PermissionsMixin
# from django.utils.datetime_safe import datetime
# from LoftStore import settings
#
#
# class CustomUserManager(UserManager):
#     def _create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError()
#         user = self.model(email = self.normalize_email(email), **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", False)
#         extra_fields.setdefault("is_superuser", False)
#         extra_fields.setdefault("is_active", False)
#         return self._create_user(email, password, **extra_fields)
#
#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#         extra_fields.setdefault("is_active", True)
#
#         if extra_fields.get("is_staff") is not True:
#             raise ValueError("Superuser must have is_staff=True")
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser must have is_superuser=True")
#         return self._create_user(email, password, **extra_fields)
#
# class UserModel(AbstractUser, PermissionsMixin):
#     username = None
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     shipping_address = models.CharField(verbose_name='Адрес доставки', max_length=254)
#     phone_number = models.CharField( verbose_name='Номер телефона', max_length=254)
#     email = models.EmailField(verbose_name='Почта', max_length=300, unique=True)
#
#     objects = CustomUserManager()
#
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'
#
#     def __str__(self):
#         return self.email
