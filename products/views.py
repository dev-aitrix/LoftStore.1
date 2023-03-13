from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework import permissions
from products.serializers import ProductModelSerializer, ProductCategorySerializer
from products.models import ProductModel, ProductCategoryModel


class ProductCategoryViews(ModelViewSet):
    queryset = ProductCategoryModel.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = (permissions.AllowAny,)


class ProductViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = (permissions.AllowAny,)
