from flask import Blueprint, request
from services.pedidos_services import obtener_pedidos, ingresar_pedidos, cambiar_estado_pedido
from utils.respuestas import respuesta_json_success, respuesta_json_fail
from utils.Validaciones import es_solo_numeros
from utils.Validaciones_pedidos import validacion_de_ingresar_pedidos, validacion_de_actualizar_estado_pedidos

pedidos = Blueprint('pedidos', __name__)


@pedidos.route('/pedidos', methods=['GET'])
def get_pedidos():
    try:
        pedidos=obtener_pedidos()
        return respuesta_json_success(pedidos, 200)

    except Exception as e:
        return respuesta_json_fail(str(e), 500)

    
@pedidos.route('/ingresar_pedidos', methods=['POST'])
def ingresar_pedido():
    try:
        
        pedido = {
            'id_producto': request.json.get('id_producto'),
            'cantidad': request.json.get('cantidad')
        }
        id_pedido=validacion_de_ingresar_pedidos(pedido)
        if id_pedido:
            return respuesta_json_fail(id_pedido, 400)
        
        return ingresar_pedidos(pedido)

    except Exception as e:
        return respuesta_json_fail(str(e), 400)
    

@pedidos.route('/actualizar_estado_pedido', methods=['PUT'])
def actualizar_pedido():
    try:
        pedido = {
            'id_pedido': request.json.get('id_pedido'),
            'estado': request.json.get('estado')
        }
        estado_pedido=validacion_de_actualizar_estado_pedidos(pedido)
        if estado_pedido:
            return respuesta_json_fail(estado_pedido, 400)
        return cambiar_estado_pedido(pedido)
    
    except Exception as e:
        return respuesta_json_fail(str(e), 400)
