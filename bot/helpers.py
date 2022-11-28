from typing import Dict


from telegram import Chat, User


def get_administrators(telegram_chat: Chat) -> Dict[int, User]:
    """Returns administrators of telegram chat"""
    return {chat_member.user.id: chat_member.user
            for chat_member in telegram_chat.get_administrators()
            if chat_member.user.is_bot is not True}
