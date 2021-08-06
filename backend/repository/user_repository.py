import typing
import db
from backend.models.user_model import User


class UserRepository:

    def __init__(self):
        pass

    def add(self, entity) -> int:
        db.UserSQL.persist(entity)
        return 1

    def getA(self, email: str) -> User:
        user = db.UserSQL.get(email=email)
        return user

    def getAll(self) -> typing.List[User]:
        user_list = db.UserSQL.find()
        return user_list

    def delete(self, entity) -> int:
        db.UserSQL.delete(entity)
        return 1
