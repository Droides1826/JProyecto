from flask import Blueprint, jsonify, request, render_template
from utils.utils import respuesta_json_success, respuesta_json_fail
from services.categorias_service import obtener_categorias, ingresar_categoria

categorias = Blueprint('categorias', __name__)

@categorias.route('/categorias', methods=['GET'])
def get_categorias():
    try:
        categorias = obtener_categorias()
        return respuesta_json_success(categorias, 200)
    except Exception as e:
        return respuesta_json_fail(str(e))

@categorias.route('/ingresar_categorias', methods=['POST'])
def create_categoria():
    try:
        valores_categoria = {
            'nombre': request.json['nombre'],
            'descripcion': request.json['descripcion']
        }
        ingresar_categoria(valores_categoria)
        return respuesta_json_success({'mensaje': 'Categoría ingresada exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@categorias.route('/index')
def index():
    return render_template('index.html')
