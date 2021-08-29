from flask import Blueprint

bp = Blueprint('api', __name__)

from backend.api import user_api, note_api, login_api
