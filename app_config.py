import os
from os import path
from pytz import timezone
from datetime import time


base_dir = path.abspath(path.dirname(__file__))


class AppConfig:
    SQL_ALCHEMY_DB_URL = f"sqlite:///{path.join(path.join(base_dir, 'app.db'))}"
    TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', None)
    MESSAGE_DELIVERY_TIME = time(hour=9, tzinfo=timezone('Europe/Samara'))
