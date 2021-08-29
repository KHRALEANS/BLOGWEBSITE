import unittest
from backend.models.note_model import Note
from backend.repository.note_repository import NoteRepository


class MyTestCase(unittest.TestCase):

    def test_can_add(self):
        note = Note(title='test2', data='add some text2', user_id=3)
        note_repository = NoteRepository()
        note_list = note_repository.findByTitle('test2')
        self.assertTrue(len(note_list) == 0)
        note_repository.add(note)
        note_list = note_repository.findByTitle('test2')
        self.assertTrue(len(note_list) > 0)


if __name__ == '__main__':
    unittest.main()
