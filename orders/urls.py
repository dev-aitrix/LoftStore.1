from django.urls import path
from orders.views import OrderViewSet, OrderedProductViewSet

app_name = 'orders'

urlpatterns = [
    path('', OrderViewSet.as_view({'get': 'list'}), name='api-OrderView'),
    path('create/', OrderViewSet.as_view({'put': 'create'}), name='api-OrderCreate'),
    path('products', OrderedProductViewSet.as_view({'get': 'list'}), name='api-OrderedProductsView'),
    path('products/create', OrderedProductViewSet.as_view({'put': 'create'}), name='api-OrderedProductsCreate'),
]