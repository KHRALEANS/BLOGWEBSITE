from flask import Flask
from flask_cors import CORS
from config import Config

from flask import Blueprint
from backend.blogweb import bp as blog_module
from backend.api import bp as api_module

from backend.repository.user_repository import UserRepository
from backend.services.user_service import UserService
import inject
import db

db.init_db()


def config_ioc(binder):
    user_repository = UserRepository()
    user_service = UserService()
    user_bind = db.UserSQL
    binder.bind(UserRepository, user_repository)
    binder.bind(UserService, user_service)
    binder.bind(db.UserSQL, user_bind)


inject.configure(config_ioc)


def create_app():
    app = Flask(__name__)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config.from_object(Config)

    app.register_blueprint(blog_module, url_prefix='/blog')
    app.register_blueprint(api_module, url_prefix='/api')
    static_module = Blueprint('static_file', __name__, static_folder="public", static_url_path="/")
    app.register_blueprint(static_module, url_prefix='/')

    return app
