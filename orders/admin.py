from django.contrib import admin
from orders.models import Order, OrderedProduct

admin.site.register(Order)
admin.site.register(OrderedProduct)
