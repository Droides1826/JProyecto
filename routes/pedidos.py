from flask import Blueprint, request
from services.pedidos_services import obtener_pedidos, ingresar_pedidos
from utils.respuestas import respuesta_json_success, respuesta_json_fail
from utils.Validaciones import es_solo_numeros,validacion_de_id_categoria ,validacion_de_precio, es_solo_letras, tiene_caracteres_especiales, limite_caracteres

pedidos = Blueprint('pedidos', __name__)

@pedidos.route('/pedidos', methods=['GET'])
def get_pedidos():
    try:
        pedidos = obtener_pedidos()
        return respuesta_json_success(pedidos,200)
    except Exception as e:
        return respuesta_json_fail(str(e))

@pedidos.route('/ingresar_pedidos', methods=['POST'])
def ingresar_pedido():
    try:
        pedido = {
            'id_producto': request.json['id_producto'],
            'cantidad': request.json['cantidad'],
            'precio_unitario': request.json['precio_unitario']
        }
        if not pedido['id_producto'] or not [pedido['cantidad']] or not pedido['precio_unitario']:
            return respuesta_json_fail('Todos los campos deben estar rellenos', 400)
        
        if not es_solo_numeros(pedido["id_producto"]) :
            return respuesta_json_fail("id_producto solo puede contener numeros.", 400)
        if not es_solo_numeros(pedido["cantidad"]) :
            return respuesta_json_fail("cantidad solo pueden contener numeros.", 400)
        if not es_solo_numeros(pedido["precio_unitario"]) :
            return respuesta_json_fail("precio unitario solo pueden contener numeros.", 400)
        
        ingresar_pedidos(pedido)
        return respuesta_json_success({'mensaje': 'Pedido ingresado exitosamente'}, 200)
    except Exception as e:
        return respuesta_json_fail(str(e), 400)
    
