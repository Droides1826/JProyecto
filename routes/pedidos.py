from flask import Blueprint, request
from services.pedidos_services import obtener_pedidos, ingresar_pedidos, cambiar_estado_pedido
from utils.respuestas import respuesta_json_success, respuesta_json_fail
from utils.Validaciones import es_solo_numeros,validacion_de_id_categoria ,validacion_de_precio, es_solo_letras, tiene_caracteres_especiales, limite_caracteres

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
        if not pedido['id_producto'] or not pedido['cantidad']:
            return respuesta_json_fail('Todos los campos deben estar rellenos', 400)
        if not es_solo_numeros(str(pedido["id_producto"])):
            return respuesta_json_fail("id_producto solo puede contener números.", 400)
        if not es_solo_numeros(str(pedido["cantidad"])):
            return respuesta_json_fail("cantidad solo puede contener números.", 400)
        
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
        if es_solo_numeros(pedido['estado']):
            return respuesta_json_fail('El estado solo puede contener letras', 400)
        if not pedido['id_pedido'] or not pedido['estado']:
            return respuesta_json_fail('Todos los campos deben estar rellenos', 400)
        if not es_solo_numeros(str(pedido["id_pedido"])):
            return respuesta_json_fail("id_pedido solo puede contener números.", 400)
        return cambiar_estado_pedido(pedido)
    
    except Exception as e:
        return respuesta_json_fail(str(e), 400)
