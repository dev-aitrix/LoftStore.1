from rest_framework.serializers import Serializer
from orders.models import Order, OrderedProduct

class OrderSerializer(Serializer):
    class Meta:
        model = Order
        exclude = ['id']

class OrderedProductSerializer(Serializer):
    class Meta:
        model = OrderedProduct
        include = '__ all__'