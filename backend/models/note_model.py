from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, Integer, DateTime
from sqlalchemy.orm import relationship
from backend.models import Base


class Note(Base):
    __tablename__: str = 'notes'

    id = Column(Integer, primary_key=True)
    data = Column(String(2000))
    date = Column(DateTime(timezone=True))
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship("User", back_populates="notes")

    def __repr__(self):
        return f"<Note(id={self.id})>"


