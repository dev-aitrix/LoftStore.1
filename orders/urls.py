from django.urls import include, path

from orders.views import OrderViewSet, OrderedProductViewSet

app_name = 'orders'
#
# orderRouter = DefaultRouter()
# orderRouter.register('Orders', OrderViewSet)
#
# orderedproductRouter = DefaultRouter()
# orderedproductRouter.register('Ordered Products', OrderedProductViewSet)


urlpatterns = [
    path('', OrderViewSet.as_view({'get': 'list'}), name='api-OrderViewSet'),
    path('products', OrderedProductViewSet.as_view({'get': 'list'}), name='api-OrderedProductsViewSet'),
]