# from django.urls import include, path
# from rest_framework.routers import DefaultRouter
#
# from products.views import
#
# app_name = 'orders'
#
# router = DefaultRouter()
# router.register('orders', views.OrderViewSet)
#
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]

from django.urls import path
from products.views import ProductViewSet
from rest_framework.routers import DefaultRouter

app_name = 'products'

productRouter = DefaultRouter()
productRouter.register('Products', ProductViewSet)

urlpatterns = [
    path('', ProductViewSet.as_view({'get': 'list'}), name='api-ProductViewSet'),
    # path('list/', views.productList, name='api-productList'),
    # path('detail/<str:pk>', views.productDetail, name='api-productDetail'),
    # path('update/<str:pk>', views.productUpdate, name='api-productUpdate'),
    # path('delete/<str:pk>', views.productDelete, name='api-productDelete'),
    # path('create', views.productCreate, name='api-productCreate'),
]
