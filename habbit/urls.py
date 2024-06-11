from django.urls import path

from habbit.apps import HabbitConfig
from habbit.views import HabbitCreateApiView, PublicHabbitListApiView, HabbitListApiView, HabbitRetrieveApiView, \
    HabbitUpdateApiView, HabbitDestroyAPIView

app_name = HabbitConfig.name


urlpatterns = [
    path('', PublicHabbitListApiView.as_view(), name='public_habbit'),
    path('habbit/', HabbitListApiView.as_view(), name='habbit_list'),
    path('habbit/create/', HabbitCreateApiView.as_view(), name='habbit_create'),
    path('habbit/<int:pk>/', HabbitRetrieveApiView.as_view(), name='read_one_habbit'),
    path('habbit/update/<int:pk>/', HabbitUpdateApiView.as_view(), name='habbit_update'),
    path('habbit/delete/<int:pk>/', HabbitDestroyAPIView.as_view(), name='habbit_delete'),
]