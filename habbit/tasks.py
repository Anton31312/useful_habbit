from django.core.mail import send_mail
from django.utils import timezone

from config import settings
from celery import app
from .models import Habbit
from .services import TelegramBot


@app.task
def check_habits_and_send_reminders():
    today = timezone.now().date()
    habbits = Habbit.objects.select_related('owner').all()
    for habbit in habbits:
        if habbit.last_completed > today:
            send_email_reminder(habbit.owner, habbit)
            send_telegram_reminder(habbit.owner, habbit)


def send_email_reminder(user, habbit):
    send_mail(
        subject='Время завершить свою привычку!',
        message=f'Пришло время выполнить свою привычку: {habbit.action}.'
                f'Вы устанавливаете, что это должно быть сделано каждый {habbit.periodicity} день.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=False,
    )


def send_telegram_reminder(user, habbit):
    if user.telegram_chat_id:
        message = f'Пришло время выполнить свою привычку: {habbit.action}.' \
                  f'Вы установили, что это будет происходить каждые {habbit.periodicity} дней.'
        TelegramBot.send_message(user.telegram_chat_id, message)
        