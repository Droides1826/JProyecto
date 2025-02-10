from utils.baseDatos import BaseDatos
from utils.respuestas import  respuesta_json_fail, respuesta_json_success

def obtener_pedidos():
        db = BaseDatos()
        pedidos = db.ejecutar_consulta("SELECT * FROM pedidos")
        return pedidos

def ingresar_pedidos(valores):
        try:
            db = BaseDatos()
            query = "INSERT INTO pedidos (id_producto, cantidad, precio_unitario) VALUES (%s, %s, %s)"
            valores = (
                valores['id_producto'],
                valores['cantidad'],
                valores['precio_unitario']
            )
            db.ejecutar_accion(query, valores)
            return respuesta_json_success({'mensaje': 'Pedido ingresado exitosamente'})
        except Exception as e:
                return respuesta_json_fail(str(e))