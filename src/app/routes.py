from urllib.parse import unquote

from flask import Blueprint, jsonify, Response, request

from app.database.database import db
from app.utils.type_specifier import TypeSpecifier


routes_blueprint = Blueprint('routes_blueprint', __name__)
collection = db["forms"]


@routes_blueprint.route('/add_form', methods=['POST'])
def add_form() -> Response:
    try:
        json_data = request.get_json()

        if 'name' in json_data.keys():
            for key, value in json_data.items():
                if key != 'name':
                    if not TypeSpecifier.is_input_type_correct(value):
                        return jsonify({'response': f'Type of field {key} is not correct! '
                                                    'Yoy can use only "date", "phone_number", "email" or "text".'})
        else:
            return jsonify({'response': 'The form must contain a name field!'})

        collection.insert_one(json_data)
        return jsonify({'response': 'Form has been added!'})

    except Exception as e:
        return jsonify(str(e))


@routes_blueprint.route('/get_form', methods=['POST'])
def get_form() -> Response:
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
