from typing import Dict

from telegram import Chat, User
from sqlalchemy.orm import Session
from sqlalchemy import select

from data_base import engine, TelegramChat


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
