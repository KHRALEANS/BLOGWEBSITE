from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, Integer, DateTime
from sqlalchemy.orm import relationship
from backend.models import Base


class User(Base):
    __tablename__: str = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(150), unique=True)
    password = Column(String(150))
    first_name = Column(String(150))

    notes = relationship("Note", order_by='Note.id', back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, password={self.password}, first_name={self.first_name})>"

    def to_json(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
            'first_name': self.first_name
        }
