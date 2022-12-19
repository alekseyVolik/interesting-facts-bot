from telegram.ext import Updater, CommandHandler

from bot.callbacks import (
    disable_daily_fact_message,
    enable_daily_fact_message,
    about_bot,
    send_random_daily_fact
)
from bot.data import BotCommandName
from app_config import AppConfig


class TelegramBotApp:

    def __init__(self, telegram_token: str) -> None:
        self.updater = Updater(telegram_token)

    def set_handlers(self) -> None:
        dispatcher = self.updater.dispatcher
        dispatcher.add_handler(CommandHandler(BotCommandName.about, about_bot))
        dispatcher.add_handler(CommandHandler(BotCommandName.disable_delivery, disable_daily_fact_message))
        dispatcher.add_handler(CommandHandler(BotCommandName.enable_delivery, enable_daily_fact_message))

    def set_jobs(self) -> None:
        job_queue = self.updater.job_queue
        job_queue.run_daily(send_random_daily_fact, AppConfig.MESSAGE_DELIVERY_TIME)

    def start(self) -> None:
        self.updater.start_polling()
        self.updater.idle()


def start_bot() -> None:
    bot = TelegramBotApp(AppConfig.TELEGRAM_BOT_TOKEN)
    print(AppConfig.TELEGRAM_BOT_TOKEN)
    bot.set_handlers()
    bot.set_jobs()
    bot.start()
