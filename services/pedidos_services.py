from utils.baseDatos import BaseDatos
from utils.respuestas import  respuesta_json_fail, respuesta_json_success

def obtener_pedidos():
    db = BaseDatos()
    query = "SELECT id_pedido, id_producto, cantidad, precio_unitario FROM pedidos"
    pedidos = db.ejecutar_consulta(query)
    pedidos_= [
        {
            "id_pedido": pedido[0],  
            "id_producto": pedido[1],
            "cantidad": pedido[2],
            "precio_unitario": float(pedido[3])
        }
        for pedido in pedidos
    ]
    return pedidos_

def ingresar_pedidos(valores):
    try:
        db = BaseDatos()
        
        producto = db.ejecutar_consulta("SELECT cantidad, precio FROM productos WHERE id_producto = %s", (valores['id_producto'],))
        
        if not producto:
            return respuesta_json_fail('El id del producto no existe en la base de datos', 400)
        
        stock_disponible = producto[0][0]  
        precio_unitario = producto[0][1]  

        if valores['cantidad'] > stock_disponible:
            return respuesta_json_fail(f'Stock insuficiente. Solo hay {stock_disponible} unidades disponibles.', 400)

        query = "INSERT INTO pedidos (id_producto, cantidad, precio_unitario) VALUES (%s, %s, %s)"
        valores_tupla = (valores['id_producto'], valores['cantidad'], precio_unitario)
        db.ejecutar_accion(query, valores_tupla)

        nuevo_stock = stock_disponible - valores['cantidad']
        db.ejecutar_accion("UPDATE productos SET cantidad = %s WHERE id_producto = %s", (nuevo_stock, valores['id_producto']))
        
        return respuesta_json_success({'mensaje': 'Pedido ingresado exitosamente'})
    except Exception as e:
        return respuesta_json_fail(str(e))
    
def cambiar_estado_pedido(pedido):
    try:
        db = BaseDatos()
        
        estado_actual = db.ejecutar_consulta("SELECT estado FROM pedidos WHERE id_pedido = %s", (pedido['id_pedido'],))
        if not estado_actual:
            return respuesta_json_fail('El id del pedido no existe en la base de datos', 400)
        
        estado_actual = estado_actual[0][0]
        estado_nuevo = pedido['estado']
        
        
        transiciones_validas = {
            'pendiente': ['enviado', 'cancelado', 'en proceso'],
            'en proceso': ['cancelado', 'enviado'],
            'cancelado': [],
            'entregado': []
        }
        
        if estado_nuevo not in transiciones_validas.get(estado_actual, []):
            return respuesta_json_fail(f'No se puede cambiar el estado de {estado_actual} a {estado_nuevo}', 400)
        
        query = "UPDATE pedidos SET estado = %s WHERE id_pedido = %s"
        valores_tupla = (estado_nuevo, pedido['id_pedido'])
        db.ejecutar_accion(query, valores_tupla)
        
        return respuesta_json_success({'mensaje': 'Estado del pedido actualizado exitosamente'})
    except Exception as e:
        return respuesta_json_fail(str(e))