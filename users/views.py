from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from users.models import User
from users.serializers import UserSerializer

class userViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
