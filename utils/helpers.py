from typing import Dict, Generator, List
from datetime import date
from urllib.parse import quote

from telegram import Chat, User
from sqlalchemy.orm import Session
from sqlalchemy import select

from db.alchemy import engine, TelegramChat
from models.models import WikipediaEvents


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


def wiki_cyrillic_link_generation(day: int, month: int) -> str:
    """
    Generate a wiki link to the 'on this day' RU-lang wiki page
    :param day: number of day
    :param month: number of month
    :return: str that represent link to page
    """
    return f'https://ru.wikipedia.org/wiki/{day}_{quote(get_month_name(month))}'


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


def generate_events_message(events: List[WikipediaEvents]) -> str:
    """
    Create message for sending to chat information about 'on this
    day' events. This message formatted with html markup
    :param events: List of events
    :return: str, message that contains list of events
    """
    today = date.today()
    message_header = (f'События, произошедшие <a href="{wiki_cyrillic_link_generation(today.day, today.month)}">'
                      f'{today.day} {get_month_name(today.month)}:</a>')
    message_body = '\n'.join(f'&#x2022 <b>{event.year}</b> &#x2014 {event.text}' for event in events)
    return f'{message_header}\n\n{message_body}'
