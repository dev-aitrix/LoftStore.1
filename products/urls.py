from django.urls import path
from products.views import ProductViewSet

app_name = 'products'

urlpatterns = [
    path('', ProductViewSet.as_view({'get': 'list'}), name='api-ProductViewSet'),
    path('create/', ProductViewSet.as_view({'put': 'create'}), name='api-ProductViewSetCreate'),
]
