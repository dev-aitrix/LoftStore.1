from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shipping_adress = models.CharField(verbose_name='Адрес доставки', max_length=1000)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=20)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
    # user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # first_name = models.CharField(max_length=50)
    # second_name = models.CharField(max_length=50)
    # email = models.CharField(max_length=320)
    # password = models.CharField(max_length=50)
    # shipping_adress = models.CharField(max_length=1000)
    # phone_number = models.CharField(max_length=20)