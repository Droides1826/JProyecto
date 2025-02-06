import re
from flask import jsonify

def respuesta_json_success(data, status=200):
    try:
        return jsonify(data), status
    except TypeError:
        return jsonify(str(data)), status

def respuesta_json_fail(message, status=400):
    return jsonify({'error': message}), status




