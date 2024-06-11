from rest_framework import serializers

from .models import Habbit
from .validators import validate_reward_and_habbit, \
    validate_enjoyable_habbit_without_reward_or_association, \
    validate_pleasant_habbit, validate_time_habbit


class HabbitSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Habbit """

    class Meta:
        model = Habbit
        fields = ['__all__']

    def validate(self, data):
        # Проверка одновременного заполнения полей вознаграждение и связанная_привычка
        validate_reward_and_habbit(
            data.get('reward'), data.get('related_habbit')
        )
        # Проверка того, что связанная привычка имеет признак приятной_привычки.
        validate_pleasant_habbit(
            data.get('related_habbit'),
            data.get('related_habbit').nice_feeling if data.get("related_habbit") else False
        )
        # Проверка того, что приятная привычка не может иметь награды или связанной с ней приятной_привычки.
        validate_enjoyable_habbit_without_reward_or_association(
            data['nice_feeling'], data.get('reward'), data.get('related_habbit')
        )
        validate_time_habbit(data['duration'])
        return data


class HabbitListSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Habbit """

    class Meta:
        model = Habbit
        fields = ['id', 'action', 'nice_feeling', 'periodicity',
                  'last_completed', 'is_public', 'owner']