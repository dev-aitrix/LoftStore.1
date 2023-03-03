from rest_framework import viewsets
from orders.serializers import OrderSerializer, OrderedProductSerializer
from orders.models import Order, OrderedProduct

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderedProductViewSet(viewsets.ModelViewSet):
    queryset = OrderedProduct.objects.all()
    serializer_class = OrderedProductSerializer
