from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions

from orders.serializers import OrderSerializer, OrderedProductSerializer
from orders.models import Order, OrderedProduct

@api_view(['GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def apiOverview(request):
    queryset = {
        'Orders List':'/list/',
        'Ordered products List':'/cart/',
    }
    return Response(queryset)

@api_view(['GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def orderList(request):
	order = Order.objects.all()
	serializer = OrderSerializer(order, many=True)
	return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def cart(request):
	op_list = OrderedProduct.objects.all()
	serializer = OrderedProductSerializer(op_list, many=True)
	return Response(serializer.data)
