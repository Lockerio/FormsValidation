from flask import Blueprint, jsonify, Response, request

from app.database import db

routes_blueprint = Blueprint('routes_blueprint', __name__)


@routes_blueprint.route('/')
def get_all_forms() -> Response:
    collections = db.list_collection_names()
    if collections:
        return jsonify({'collections': collections})
    else:
        return jsonify({'response': 'no such collections'})
