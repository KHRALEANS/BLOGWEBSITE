import inject
from flask import request, jsonify
from backend.models.note_model import Note
from backend.services.note_service import NoteService
from backend.api import bp
import os

note_service = inject.instance(NoteService)


@bp.route('/note/create/', methods=['POST'])
def create_note():
    title = request.json['title']
    data = request.json['data']
    user_id = request.json['user_id']

    note = Note(title=title, data=data, user_id=user_id)
    note_service.add(note)

    return jsonify(note.to_json())


@bp.route('/notes', methods=['GET'])
def list_notes():
    note_list = note_service.getAll()

    result = {
        'notes': [item.to_json() for item in note_list]
    }

    return jsonify(result)


@bp.route('/note/<noteId>', methods=['GET'])
def get_note(noteId):
    with open('./backend/data/3.md', 'r') as file:
        note = file.read()

    return jsonify(note)

