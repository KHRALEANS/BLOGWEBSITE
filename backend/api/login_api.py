from backend.api import bp
from flask import request, make_response, jsonify
import jwt
import datetime
import settings
from functools import wraps


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, settings.JwtKey, algorithms=["HS256"])
        except jwt.DecodeError:
            return jsonify({'message': 'Token is invalid!'}), 403
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token is expired!'}), 403
        else:
            return f(*args, **kwargs)

    return decorated


@bp.route('/login')
def login():
    auth = request.authorization

    if auth and auth.password == '12345678':
        token = jwt.encode(
            {'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)},
            settings.JwtKey, algorithm="HS256")
        return jsonify({'token': token})
    return make_response('could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})


@bp.route('/unprotected')
def unprotected():
    return jsonify({'message': 'Anyone can view this!'})


@bp.route('/protected')
@token_required
def protected():
    return jsonify({'message': 'viewed by valid tokens.'})
