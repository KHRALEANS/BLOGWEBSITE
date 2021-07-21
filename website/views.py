import time

import flask_login
from website.auth import login
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
from .models import Note
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('笔记太短了', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            # test
            print(f'ready to add note by user {current_user.id}')

            db.session.add(new_note)
            db.session.commit()
            flash('添加了一条笔记！', category='success')
    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST', 'GET'])
def delete_note():
    data = json.loads(request.data)
    print(data)
    note_id = data['noteId']
    print(note_id)
    current_user_id = data['userId']
    note = Note.query.get(note_id)
    print(note.user_id)
    print(current_user_id)
    if note:
        if note.user_id == int(current_user_id):
            print("ready to delete")
            db.session.delete(note)
            db.session.commit()
            flash('删除成功！', category='success')

    return jsonify({})
