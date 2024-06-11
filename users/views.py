from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from habbit.permissions import IsOwner
from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        # Возвращает соответствующие разрешения в зависимости от действия.
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        elif self.action == 'list' or self.action == 'destroy' or self.action == 'update' or self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated, IsOwner]
        else:
            self.action = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]