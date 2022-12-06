from typing import Dict, Generator
import re
from datetime import date
from urllib.parse import quote

from telegram import Chat, User
from sqlalchemy.orm import Session
from sqlalchemy import select

from data_base import engine, TelegramChat
from models import WikipediaSelectedEvents


def get_administrators(telegram_chat: Chat) -> Dict[int, User]:
    """Returns administrators of telegram chat"""
    return {chat_member.user.id: chat_member.user
            for chat_member in telegram_chat.get_administrators()
            if chat_member.user.is_bot is not True}


def change_enable_fact_delivery(chat_id: int,
                                delivery_fact: bool
                                ) -> None:
    """
    To use for change enable or disable 'On This Day' message
    delivery. This command creates a record in DB to save
    information about the telegram chat
    :param chat_id: telegram id of chat
    :param delivery_fact: True (enable) or False (disable) delivery
    :return:
    """
    with Session(engine) as session:
        query_result = session.execute(select(TelegramChat)
                                       .where(TelegramChat.chat_id == chat_id))
        telegram_chat = query_result.scalar_one_or_none()
        if telegram_chat:
            telegram_chat.receive_fact = delivery_fact
        else:
            session.add(TelegramChat(chat_id=chat_id, receive_fact=delivery_fact))
        session.commit()


def get_chat_ids_for_delivery() -> Generator[int, None, None]:
    """
    It is yielding telegram chat ids that have are
    enabled delivery the 'on this day' message
    """
    with Session(engine) as session:
        query_result = session.execute(select(TelegramChat.chat_id))
        for chat_id in query_result.scalars():
            yield chat_id


def prepare_message_with_markdown_v2(event: WikipediaSelectedEvents) -> str:
    """
    Prepare wikipedia event description text for markdown_v2
    escaping the special chars '_*[]()~`>#+-=|{}.!'. If somewhat
    is matches exactly (by symbol register too) by wikipedia link
    this text will be replaced to Markdown link
    :param event: WikipediaEvent
    :return: Formatted text for send with markdown_v2 method
    """
    escape_chars = '_*[]()~`>#+-=|{}.!'
    event_description = re.sub(f'([{re.escape(escape_chars)}])', r'\\\1', event.text)
    return event_description


def wiki_cyrillic_link_generation() -> str:
    """
    Generate a wiki link to the 'on this day' RU-lang wiki page
    :return: str that represent link to page
    """
    today = date.today()
    return f'https://ru.wikipedia.org/wiki/{today.day}_{quote(get_month_name(today.month))}'


def get_month_name(month: int) -> str:
    """
    Return ru-lang name of month
    :param month: number of month from 1 to 12
    :return: str of RU-lang month name
    """
    month_name_map = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля',
                      5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа',
                      9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'}
    return month_name_map[month]
