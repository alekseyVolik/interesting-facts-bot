from sqlalchemy.orm import declarative_base
from sqlalchemy import (
    Column,
    Integer, Boolean,
    create_engine
)


from app_config import AppConfig


engine = create_engine(AppConfig.SQL_ALCHEMY_DB_URL)


Base = declarative_base()


class TelegramChat(Base):
    __tablename__ = "telegram_chat"

    _id = Column(Integer, primary_key=True)
    chat_id = Column(Integer)
    receive_fact = Column(Boolean)

    def __repr__(self):
        return f'TelegramChat(_id={self._id}, chat_id={self.chat_id}, receive_fact={self.receive_fact})'
