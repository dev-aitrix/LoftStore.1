from django.db import models
from users.models import User
from products.models import Product
import uuid

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Заказавший пользователь')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    total_cost = models.DecimalField(verbose_name='Сумма заказа', max_digits=9, decimal_places=2)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.user


class OrderedProduct(models.Model):
    order = models.ForeignKey(Order, verbose_name='id заказа', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='id товара',  on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name='количество заказанных товаров')

    class Meta:
        verbose_name = 'Заказанный товар'
        verbose_name_plural = 'Заказанные товары'

    def __str__(self):
        return self.order