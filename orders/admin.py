from django.contrib import admin
from orders.models import Order, OrderedProduct

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'total_cost',)
    search_fields = ('user',)
    list_filter = ('date',)
    empty_value_display = '-пусто-'


@admin.register(OrderedProduct)
class OrderedProductAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'count',)
    search_fields = ('product',)
    empty_value_display = '-пусто-'