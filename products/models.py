from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Наименование', max_length=1000)
    сategory = models.CharField(verbose_name='Категория', max_length=1000)
    description = models.TextField(verbose_name='Описание', max_length=20000)
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=2)
    count = models.IntegerField(verbose_name='Количество',)
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name