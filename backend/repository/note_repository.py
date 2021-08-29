import typing

import db
from backend.models.note_model import Note


class NoteRepository:

    def __init__(self):
        pass

    def add(self, entity) -> int:
        db.NoteSQL.persist(entity)
        return 1

    def delete(self, entity) -> int:
        db.NoteSQL.persist(entity)
        return 1

    def findByTitle(self, title: str) -> typing.List[Note]:
        note_list = db.NoteSQL.find2(Note.title == title)
        return note_list

    def findByUser(self, user_id: int) -> typing.List[Note]:
        note_list = db.NoteSQL.find2(Note.user_id == user_id)
        return note_list

    def all(self) -> typing.List[Note]:
        note_list = db.NoteSQL.find()
        return note_list
