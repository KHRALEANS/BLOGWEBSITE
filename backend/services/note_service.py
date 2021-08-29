import inject
import typing
from backend.models.note_model import Note
from backend.repository.note_repository import NoteRepository


class NoteService:

    note_repository = inject.attr(NoteRepository)

    def add(self, entity) -> int:
        self.note_repository.add(entity)
        return 1

    def delete(self, entity) -> int:
        self.note_repository.delete(entity)
        return 1

    def findByTitle(self, title: str) -> typing.List[Note]:
        note_list = self.note_repository.findByTitle(title)
        return note_list

    def findByUser(self, user_id: int) -> typing.List[Note]:
        note_list = self.note_repository.findByUser(user_id)
        return note_list

    def getAll(self) -> typing.List[Note]:
        note_list = self.note_repository.all()
        return note_list
