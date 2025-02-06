from flask import Blueprint, jsonify
from services.pedidos_services import obtener_pedidos 
from utils.utils import respuesta_json_success, respuesta_json_fail

pedidos = Blueprint('pedidos', __name__)

@pedidos.route('/pedidos', methods=['GET'])
def get_pedidos():
    try:
        pedidos = obtener_pedidos()
        return respuesta_json_success(pedidos,200)
    except Exception as e:
        return respuesta_json_fail(str(e))

