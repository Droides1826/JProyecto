from utils.baseDatos import BaseDatos

def obtener_pedidos():
        db = BaseDatos()
        pedidos = db.ejecutar_consulta("SELECT * FROM pedidos")
        return pedidos
    


