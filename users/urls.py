from django.urls import path
from users.views import userViewSet

urlpatterns = [
    path('', userViewSet.as_view({'get': 'list'}), name='api-UserViewSet'),
]