from django.contrib import admin

from habbit.models import Habbit


@admin.register(Habbit)
class HabbitAdmin(admin.ModelAdmin):
    list_display = ('pk', 'owner', 'action', 'nice_feeling', 'periodicity', 'last_completed', 'is_public')
    