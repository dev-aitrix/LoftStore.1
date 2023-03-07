from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from users.models import UserModel
from users.serializers import UserSerializer

class userViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)