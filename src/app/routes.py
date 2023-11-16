from flask import Blueprint, jsonify, Response, request

from app.database.database import db

routes_blueprint = Blueprint('routes_blueprint', __name__)


@routes_blueprint.route('/')
def get_all_forms() -> Response:
    collections = db.list_collection_names()
    if collections:
        return jsonify({'collections': collections})
    else:
        return jsonify({'response': 'no such collections'})


@routes_blueprint.route('/get_form', methods=['POST'])
def get_form() -> Response:
    query_params = request.args
    collection = db["forms"]

    filter_query = {field: query_params[field] for field in query_params}

    result = list(collection.find(filter_query))
    return jsonify(result)

