from telegram import Update
from telegram.ext import CallbackContext

from bot.data import MessageTemplate, BotCommandName
from utils.api_wrap import OnThisDayAPIWrap
from utils.helpers import (
    get_administrators,
    change_enable_fact_delivery,
    get_chat_ids_for_delivery
)
from app_config import AppConfig


def about_bot(update: Update,
              context: CallbackContext
              ) -> None:
    """Send to telegram chat information about bot"""
    bot = context.bot
    chat_id = update.effective_chat.id
    text = MessageTemplate.about_bot.format(command=BotCommandName.enable_delivery)

    bot.send_message(chat_id=chat_id, text=text)


def send_random_daily_fact(context: CallbackContext) -> None:
    """Send random daily fact from REST-API wikipedia 'on this day'"""
    bot = context.bot
    events = OnThisDayAPIWrap().get_fact_about_today_day()
    for chat_id in get_chat_ids_for_delivery():
        event = events.get_random_event()
        text = event.description
        bot.send_message(chat_id=chat_id, text=text)


def enable_daily_fact_message(update: Update,
                              context: CallbackContext
                              ) -> None:
    """Turn on for sending 'on this day' message"""
    bot = context.bot
    user = update.effective_user
    chat = update.effective_chat
    administrators = get_administrators(telegram_chat=chat)

    if user.id in administrators.keys():
        change_enable_fact_delivery(chat_id=chat.id, delivery_fact=True)
        text = MessageTemplate.subscribes_delivery.format(time=AppConfig.MESSAGE_DELIVERY_TIME.strftime('%H:%M'),
                                                          command=BotCommandName.disable_delivery)
        bot.send_message(chat_id=chat.id, text=text)
    else:
        text = MessageTemplate.only_administrator_right.format(command=BotCommandName.enable_delivery)
        update.message.reply_text(text=text)


def disable_daily_fact_message(update: Update,
                               context: CallbackContext
                               ) -> None:
    """Turn off for sending 'on this day' message"""
    bot = context.bot
    user = update.effective_user
    chat = update.effective_chat
    administrators = get_administrators(telegram_chat=chat)

    if user.id in administrators.keys():
        change_enable_fact_delivery(chat_id=chat.id, delivery_fact=False)
        text = MessageTemplate.unsubscribe_delivery
        bot.send_message(chat_id=chat.id, text=text)
    else:
        text = MessageTemplate.only_administrator_right.format(command=BotCommandName.disable_delivery)
        update.message.reply_text(text=text)
