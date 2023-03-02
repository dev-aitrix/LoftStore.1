from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    shipping_address = models.CharField(verbose_name='Адрес доставки', max_length=254)
    phone_number = models.CharField( verbose_name='Номер телефона', max_length=254)
    email = models.EmailField(verbose_name='Почта', max_length=300, unique=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email