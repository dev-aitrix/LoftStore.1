from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from products.serializers import ProductModelSerializer
from products.models import ProductModel

class ProductViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
