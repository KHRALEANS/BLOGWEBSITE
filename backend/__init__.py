import inject
import db

from backend.repository.user_repository import UserRepository
from backend.repository.note_repository import NoteRepository

from backend.services.user_service import UserService
from backend.services.note_service import NoteService

#db.init_db()


def config_ioc(binder):
    user_repository = UserRepository()
    note_repository = NoteRepository()

    user_service = UserService()
    note_service = NoteService()

    user_bind = db.UserSQL
    note_bind = db.NoteSQL

    binder.bind(UserRepository, user_repository)
    binder.bind(NoteRepository, note_repository)

    binder.bind(UserService, user_service)
    binder.bind(NoteService, note_service)

    binder.bind(db.UserSQL, user_bind)
    binder.bind(db.NoteSQL, note_bind)


inject.configure(config_ioc)

from flask import Flask
from flask_cors import CORS
from config import Config

from flask import Blueprint
from backend.blogweb import bp as blog_module
from backend.api import bp as api_module


def create_app():
    db.init_db()
    app = Flask(__name__)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config.from_object(Config)
    app.config['SECRET_KEY'] = 'thisisthesecretkey'

    app.register_blueprint(blog_module, url_prefix='/blog')
    app.register_blueprint(api_module, url_prefix='/api')
    static_module = Blueprint('static_file', __name__, static_folder="public", static_url_path="/")
    app.register_blueprint(static_module, url_prefix='/')

    return app
