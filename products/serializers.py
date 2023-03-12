from rest_framework.serializers import ModelSerializer
from products.models import ProductModel


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        exclude = ['id']
