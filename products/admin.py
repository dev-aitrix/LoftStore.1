from django.contrib import admin
from .models import ProductModel

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'category', 'price',)
    search_fields = ('name',)
    list_filter = ('category',)
    empty_value_display = '-пусто-'