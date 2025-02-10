from flask import Blueprint, request
from services.pedidos_services import obtener_pedidos 
from utils.respuestas import respuesta_json_success, respuesta_json_fail

pedidos = Blueprint('pedidos', __name__)

@pedidos.route('/pedidos', methods=['GET'])
def get_pedidos():
    try:
        pedidos = obtener_pedidos()
        return respuesta_json_success(pedidos,200)
    except Exception as e:
        return respuesta_json_fail(str(e))

@pedidos.route('/ingresar_pedidos', methods=['POST'])
def ingresar_pedidos():
    try:
        valores_pedidos = {
            'id_producto': request.json['id_producto'],
            'cantidad': request.json['cantidad'],
            'total': request.json['total'],
            'fecha': request.json['fecha'],
            'estado': request.json['estado']
        }
        ingresar_pedidos(valores_pedidos)
        return respuesta_json_success({'mensaje': 'Pedido ingresado exitosamente'}, 200)
    except Exception as e:
        return respuesta_json_fail(str(e), 400)