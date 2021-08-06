import inject
import typing
from backend.models.user_model import User
from backend.repository.user_repository import UserRepository


class UserService:

    user_repository = inject.attr(UserRepository)

    def add(self, entity) -> int:
        self.user_repository.add(entity)
        return 1

    def delete(self, entity) -> int:
        self.user_repository.delete(entity)
        return 1

    def getA(self, email: str) -> User:
        user = self.user_repository.getA(email)
        return user

    def getAll(self) -> typing.List[User]:
        user_list = self.user_repository.getAll()
        return user_list
