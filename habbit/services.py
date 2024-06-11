import requests

from config import settings


class TelegramBot:
    URL = 'https://api.telegram.org/bot'
    TOKEN = settings.API_TELEGRAM_TOKEN

    @classmethod
    def send_message(cls, chat_id, text):
        response = requests.post(
            url=f'{cls.URL}{cls.TOKEN}/sendMessage',
            data={
                'chat_id': chat_id,
                'text': text
            }
        )
        response.raise_for_status()
        