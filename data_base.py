from sqlalchemy.orm import declarative_base
from sqlalchemy import (
    Column,
    Integer, String, Boolean
)


Base = declarative_base()


class TelegramChat(Base):
    __tablename__ = "telegram_chat"

    _id = Column(Integer, primary_key=True)
    chat_id = Column(String(20))
    receive_fact = Column(Boolean)
