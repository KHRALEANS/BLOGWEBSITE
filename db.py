from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config

from backend.models.note_model import Note
from backend.models.user_model import User
from backend.repository.base_repository import FSQLAlchemyRepository

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
DBSession = sessionmaker(bind=engine)
session = DBSession()

NoteSQL = FSQLAlchemyRepository(Note, session)
UserSQL = FSQLAlchemyRepository(User, session)

from backend.models import my_metadata


def init_db():
    """
    首次运行：
    $ python
    >>> import db
    >>> db.init_db()
    建立数据表
    """
    my_metadata.create_all(bind=engine)
