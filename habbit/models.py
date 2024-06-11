from django.db import models
from config import settings

NULLABLE = {'null': True, 'blank': True}


class Habbit(models.Model):
    """ Модель полезной привычки """
    action = models.CharField(max_length=255, verbose_name='действие')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='владелец', null=True)
    nice_feeling = models.BooleanField(default=False, verbose_name='приятная привычка?')
    periodicity = models.IntegerField(default=7, verbose_name='периодичность выполнения привычки (в днях)')
    last_completed = models.DateField(verbose_name='последний раз', **NULLABLE)
    is_public = models.BooleanField(default=True, verbose_name="доступно для других?")
    place = models.CharField(max_length=255, verbose_name='место действия')
    duration = models.DurationField(verbose_name='время выполнения привычки')
    related_habbit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='связанная привычка', **NULLABLE)
    reward = models.CharField(max_length=255, verbose_name='вознаграждение', **NULLABLE)

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
