from utils import Validaciones


def validacion_de_ingresar_pedidos(valores_pedidos):
    if not valores_pedidos["id_producto"] or not valores_pedidos["cantidad"]:
        return "El ID del producto y la cantidad son obligatorios."
    if not Validaciones.es_solo_numeros(valores_pedidos["id_producto"]):
        return "El ID del producto debe ser un número."
    if not Validaciones.es_solo_numeros(valores_pedidos["cantidad"]):
        return "La cantidad debe ser un número."
    return None

def validacion_de_actualizar_estado_pedidos(valores_pedidos):
    if not valores_pedidos["id_pedido"] or not valores_pedidos["estado"]:
        return "El ID del pedido y el estado son obligatorios."
    if not Validaciones.es_solo_numeros(valores_pedidos["id_pedido"]):
        return "El ID del pedido debe ser un números."
    if  Validaciones.es_solo_numeros(valores_pedidos["estado"]):
        return "El estado del pedido solo puede ser PENDIENTE-EN PROCESO-ENVIADO/CANCELADO."
     
    return None