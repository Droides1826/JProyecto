from utils.baseDatos import BaseDatos
from utils.respuestas import  respuesta_json_fail, respuesta_json_success

def obtener_pedidos():
        db = BaseDatos()
        pedidos = db.ejecutar_consulta("SELECT * FROM pedidos")
        return pedidos

def ingresar_pedidos(valores):
    try:
        db = BaseDatos()
        producto = db.ejecutar_consulta("SELECT * FROM productos WHERE id_producto = %s", (valores['id_producto'],))
        if not producto:
            return respuesta_json_fail('El id del producto no existe en la base de datos')
        query = "INSERT INTO pedidos (id_producto, cantidad, precio_unitario) VALUES (%s, %s, %s)"
        valores_tupla = (
            valores['id_producto'],
            valores['cantidad'],
            valores['precio_unitario']
        )

        db.ejecutar_accion(query, valores_tupla)
        return respuesta_json_success({'mensaje': 'Pedido ingresado exitosamente'})

    except Exception as e:
        return respuesta_json_fail(str(e))
