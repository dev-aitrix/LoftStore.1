from django.urls import path
from products import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('list/', views.productList, name='api-productList'),
    # path('detail/<str:pk>', views.productDetail, name='api-productDetail'),
    # path('update/<str:pk>', views.productUpdate, name='api-productUpdate'),
    # path('delete/<str:pk>', views.productDelete, name='api-productDelete'),
    # path('create', views.productCreate, name='api-productCreate'),
]
