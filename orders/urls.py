from django.urls import include, path
from rest_framework.routers import DefaultRouter

from orders.views import OrderViewSet, OrderedProductViewSet

app_name = 'orders'

orderRouter = DefaultRouter()
orderRouter.register('Orders', OrderViewSet)

orderedproductRouter = DefaultRouter()
orderedproductRouter.register('Ordered Products', OrderedProductViewSet)


urlpatterns = [
    # path('', include(orderRouter.urls)),
    # path('', include(orderedproductRouter.urls)),
    path('', OrderViewSet.as_view({'get': 'list'}), name='api-OrderViewSet'),
    path('products', OrderedProductViewSet.as_view({'get': 'list'}), name='api-OrderedProductsViewSet'),
]