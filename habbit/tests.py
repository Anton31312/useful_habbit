from datetime import datetime

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from habbit.models import Habbit
from users.models import User


class HabbitAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@test.ru')
        self.user.set_password('test_pass123')
        self.user.save()

        self.client.force_authenticate(user=self.user)

        self.public_habbit = Habbit.objects.create(
            owner=self.user,
            place='Тестовое место',
            duration='00:01:00',
            action='Тестовое действие',
            nice_feeling=False,
            periodicity=1,
            reward='Тестовое вознаграждение',
            last_completed=datetime.utcnow(),
            is_public=True,
        )

    def test_habbit_my_list(self):
        """ Тестирование вывода списка привычек """

        response = self.client.get(reverse('habbit:habbit_list'))
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results': [
                    {
                        "id": self.public_habbit.id,
                        "action": self.public_habbit.action,
                        "nice_feeling": self.public_habbit.nice_feeling,
                        "periodicity": self.public_habbit.periodicity,
                        "last_completed": self.public_habbit.last_completed.strftime("%Y-%m-%d"),
                        "is_public": self.public_habbit.is_public,
                        "owner": self.public_habbit.owner.id,
                    }
                ]
            }
        )

    def test_habbit_detail(self):
        """ Тестирование получения привычки """

        response = self.client.get(
            reverse('habbit:read_one_habbit', args=[self.public_habbit.id]))
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {
                "id": self.public_habbit.id,
                "action": self.public_habbit.action,
                "nice_feeling": self.public_habbit.nice_feeling,
                "periodicity": self.public_habbit.periodicity,
                "last_completed": self.public_habbit.last_completed.strftime("%Y-%m-%d"),
                "is_public": self.public_habbit.is_public,
                "owner": self.public_habbit.owner.id,
                "place": self.public_habbit.place,
                "duration": self.public_habbit.duration,
                "related_habbit": self.public_habbit.related_habbit,
                "reward": self.public_habbit.reward
            }
        )

    def test_habbit_create(self):
        """ Тестирования создания привычки """

        data = dict(
            owner=self.user.id,
            place='Тестовое место 2',
            duration='00:00:20',
            action='Тестовое действие 2',
            nice_feeling=False,
            periodicity='1',
            reward='Тестовое вознаграждение 2',
            last_completed=datetime.utcnow().strftime("%Y-%m-%d"),
            is_public=True,
        )
        response = self.client.post(reverse('habbit:habbit_create'), data=data)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(Habbit.objects.count(), 2)

    def test_habbit_create_with_related_habit(self):
        """ Тестирования создания привычки с родителем """
        habbit = Habbit.objects.create(
            owner=self.user,
            place='Тестовое место',
            duration='00:00:60',
            action='Тестовое действие',
            nice_feeling=True,
            periodicity=1,
            last_completed=datetime.utcnow(),
            is_public=True,
        )
        data = dict(
            owner=self.user.id,
            place='Тестовое место 2',
            duration='00:00:60',
            action='Тестовое действие 2',
            nice_feeling=False,
            periodicity='1',
            last_completed=datetime.utcnow().strftime("%Y-%m-%d"),
            is_public=True,
            related_habbit=habbit.id
        )
        response = self.client.post(reverse('habbit:habbit_create'), data=data)
        self.assertEqual(response.status_code, 201)

    def test_habbit_update(self):
        """ Тестирование обновления привычки """

        data = dict(
            place='Тестовое место 4',
            duration='00:00:20',
            action='Тестовое действие 4',
            nice_feeling=False,
            periodicity=1,
            reward='Тестовое вознаграждение 4',
            is_public=True,
        )
        response = self.client.patch(reverse('habbit:habbit_update', args=[self.public_habbit.id]), data=data)        
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {
                "id": self.public_habbit.id,
                "action": data['action'],
                "nice_feeling": data['nice_feeling'],
                "periodicity": data['periodicity'],
                "is_public": data['is_public'],
                "owner": self.public_habbit.owner.id,
                "last_completed": self.public_habbit.last_completed.strftime("%Y-%m-%d"),
                "place": data['place'],
                "duration": data['duration'],
                "related_habbit": self.public_habbit.related_habbit,
                "reward": data['reward'],
            }
        )

    def test_habbit_destroy(self):
        """ Тестирование удаления привычки """

        response = self.client.delete(reverse('habbit:habbit_delete', args=[self.public_habbit.id]))
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(Habbit.objects.count(), 0)
