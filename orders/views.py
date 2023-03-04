from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from orders.serializers import OrderSerializer, OrderedProductSerializer
from orders.models import Order, OrderedProduct

class OrderViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class OrderedProductViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = OrderedProduct.objects.all()
    serializer_class = OrderedProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
