from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from habbit.models import Habbit
from habbit.paginators import HabbitPaginator
from habbit.permissions import IsOwner
from habbit.serializers import HabbitSerializer, HabbitListSerializer


class PublicHabbitListApiView(generics.ListAPIView):
    """ Список доступных привычек """
    serializer_class = HabbitSerializer
    pagination_class = HabbitPaginator
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Habbit.objects.filter(is_public=True)


class HabbitListApiView(generics.ListAPIView):
    """ Список привычек пользователя"""
    serializer_class = HabbitListSerializer
    pagination_class = HabbitPaginator

    def get_queryset(self):
        user = self.request.user
        return Habbit.objects.filter(owner=user.id).order_by('id')


class HabbitCreateApiView(generics.CreateAPIView):
    """ Создание привычки """
    queryset = Habbit.objects.all()
    serializer_class = HabbitSerializer
    permission_classes = [IsAuthenticated]


class HabbitRetrieveApiView(generics.RetrieveAPIView):
    """ Чтение привычки """
    queryset = Habbit.objects.all()
    serializer_class = HabbitSerializer
    permission_classes = [IsAuthenticated | IsOwner]


class HabbitUpdateApiView(generics.UpdateAPIView):
    """ Обновление привычки """
    queryset = Habbit.objects.all()
    serializer_class = HabbitSerializer
    permission_classes = [IsAuthenticated]


class HabbitDestroyAPIView(generics.DestroyAPIView):
    """ Удаление привычки"""
    queryset = Habbit.objects.all()
    serializer_class = HabbitSerializer
    permission_classes = [IsAuthenticated | IsOwner]
    