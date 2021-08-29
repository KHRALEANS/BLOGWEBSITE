from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, Integer, DateTime
from sqlalchemy.orm import relationship
from backend.models import Base
import datetime


class Note(Base):
    __tablename__: str = 'notes'

    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    data = Column(String(2000))
    date = Column(DateTime(timezone=True), default=datetime.datetime.now())
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship("User", back_populates="notes")

    def __repr__(self):
        return f"<Note(id={self.id})>"

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'data': self.data,
            'date': self.date,
            'user_id': self.user_id
        }
