from urllib.parse import unquote

from flask import Blueprint, jsonify, Response, request

from app.database.database import db
from app.utils.type_specifier import TypeSpecifier


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
    collection = db["forms"]
    query_string = request.query_string.decode('utf-8')
    filter_query = {'response': 'You did not enter any query parameters!'}

    if query_string:
        decoded_query_string = unquote(query_string)
        query_params = {
            x: y
            for x, y in (param_string.split("=")
                         for param_string in decoded_query_string.split("&"))
        }

        filter_query = {field: TypeSpecifier.define_input_type(query_params[field]) for field in query_params}

        result = list(collection.find(filter_query))
    else:
        result = list(collection.find())

    if result:
        for item in result:
            item['_id'] = str(item['_id'])
        return jsonify(result)
    else:
        return jsonify(filter_query)
