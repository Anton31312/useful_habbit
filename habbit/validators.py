from datetime import timedelta

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from habbit.models import Habbit


def validate_reward_and_habbit(reward, related_habbit):
    """Проверка одновременного заполнения полей вознаграждение и связанной привычки"""
    if reward and related_habbit:
        raise ValidationError(_('Вы не можете указать вознаграждение и связанную с ним привычку одновременно.'))


def validate_pleasant_habbit(related_habbit, nice_feeling):
    """Проверка того, что связанная привычка имеет признак приятной привычки."""
    if related_habbit and not nice_feeling:
        raise ValidationError(
            _('Сопутствующими привычками могут быть только те, которые имеют характеристики приятной привычки.'))


def validate_enjoyable_habbit_without_reward_or_association(nice_feeling, reward, related_habbit):
    """Проверка того, что приятная привычка не может иметь награды или связанной с ней привычки."""
    try:
        if nice_feeling:
            if related_habbit or reward:
                raise ValidationError(
                    _('Приятная привычка не может иметь вознаграждения или связанной с ней привычки.'))
    except KeyError:
        pass


def validate_time_habbit(duration):
    """Проверка того, что привычка не может быть дольше 120 секунд."""
    time = timedelta(minutes=2)
    if duration > time:
        raise ValidationError('Привычку можно выполнять не более 120 секунд.')
    
def validate_periodicity_habbit(periodicity):
    """Проверка того, что привычка не может быть выполнена реже, чем 1 раз в 7 дней."""
    if periodicity < 1:
        raise ValidationError('Привычку можно выполнять не реже, чем 1 раз в 7 дней.')    