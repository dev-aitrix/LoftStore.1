from rest_framework import viewsets
from products.serializers import ProductSerializer
from products.models import Product

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from rest_framework import permissions
#
# from products.serializers import ProductSerializer
# from products.models import Product
#
#
# @api_view(['GET'])
# @permission_classes((permissions.IsAuthenticatedOrReadOnly,))
# def apiOverview(request):
# 	api_urls = {
# 		'List':'/list/',
# 		# 'Detail View':'/detail/<str:pk>/',
# 		# 'Create':'/create/',
# 		# 'Update':'/update/<str:pk>/',
# 		# 'Delete':'/delete/<str:pk>/',
# 		}
#
# 	return Response(api_urls)
#
# @api_view(['GET'])
# @permission_classes((permissions.IsAuthenticatedOrReadOnly,))
# def productList(request):
# 	product = Product.objects.all().order_by('-id')
# 	serializer = ProductSerializer(product, many=True)
# 	return Response(serializer.data)
