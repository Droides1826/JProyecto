from utils.baseDatos import BaseDatos
from utils.respuestas import respuesta_json_success, respuesta_json_fail

def obtener_pedidos():
        db = BaseDatos()
        pedidos = db.ejecutar_consulta("SELECT * FROM pedidos")
        return pedidos
    


