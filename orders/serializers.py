from rest_framework.serializers import ModelSerializer
from orders.models import Order, OrderedProduct

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        exclude = ['id']

class OrderedProductSerializer(ModelSerializer):
    class Meta:
        model = OrderedProduct
        fields = ('__all__')