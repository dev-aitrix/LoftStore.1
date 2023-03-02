from django.urls import path
from orders import views

urlpatterns = [
    path('', views.apiOverview, name='api-view'),
    path('list/', views.orderList, name='api-orderList'),
    path('cart/', views.cart, name='api-cart'),
]