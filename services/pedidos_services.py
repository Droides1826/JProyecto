from utils.baseDatos import BaseDatos
from utils.respuestas import  respuesta_json_fail, respuesta_json_success

def obtener_pedidos():
    db = BaseDatos()
    query = """
    SELECT p.id_pedido, pr.nombre, p.cantidad, p.precio_unitario, p.valor_total
    FROM pedidos p
    JOIN productos pr ON p.id_producto = pr.id_producto
    """
    pedidos = db.ejecutar_consulta(query)
    pedidos_ = [
        {
            "id_pedido": pedido[0],
            "nombre_producto": pedido[1],
            "cantidad": pedido[2],
            "precio_unitario": pedido[3],
            "valor_total": pedido[4]
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
        
        stock_disponible = int(producto[0][0])
        precio_unitario = float(producto[0][1])

        cantidad = int(valores['cantidad'])

        if cantidad > stock_disponible:
            return respuesta_json_fail(f'Stock insuficiente. Solo hay {stock_disponible} unidades disponibles.', 400)

        query = "INSERT INTO pedidos (id_producto, cantidad, precio_unitario) VALUES (%s, %s, %s)"
        valores_tupla = (valores['id_producto'], cantidad, precio_unitario)
        db.ejecutar_accion(query, valores_tupla)

        nuevo_stock = stock_disponible - cantidad
        db.ejecutar_accion("UPDATE productos SET cantidad = %s WHERE id_producto = %s", (nuevo_stock, valores['id_producto']))
        
        return respuesta_json_success({'mensaje': 'Pedido ingresado exitosamente'})
    except Exception as e:
        return respuesta_json_fail(str(e))
    
def cambiar_estado_pedido(pedido):
    try:
        db = BaseDatos()

        estado_actual = db.ejecutar_consulta("SELECT estado FROM pedidos WHERE id_pedido = %s", (pedido['id_pedido'],))
        if not estado_actual:
            return respuesta_json_fail('El ID del pedido no existe en la base de datos', 400)

        estado_actual = estado_actual[0][0]  
        
        estados_validos = {
            'pendiente': 3, 'en proceso': 4, 'enviado': 5, 'cancelado': 6,
            3: 'pendiente', 4: 'en proceso', 5: 'enviado', 6: 'cancelado'
        }

        estado_nuevo = estados_validos.get(pedido['estado'].lower())
        if estado_nuevo is None:
            return respuesta_json_fail('Estado inválido. Debe ser: pendiente, en proceso, enviado o cancelado', 400)


        transiciones_validas = {
            3: [4, 6],  
            4: [5, 6],      
            5: [],          
            6: []           
        }
        if estado_nuevo not in transiciones_validas.get(estado_actual, []):
            return respuesta_json_fail(f'No se puede cambiar el estado de {estados_validos[estado_actual]} a {estados_validos[estado_nuevo]}, Orden de los estados: PENDIENTE-EN PROCESO-ENVIADO/CANCELADO', 400)
        query = "UPDATE pedidos SET estado = %s WHERE id_pedido = %s"
        db.ejecutar_accion(query, (estado_nuevo, pedido['id_pedido']))

        return respuesta_json_success({'mensaje': 'Estado del pedido actualizado exitosamente a ' + estados_validos[estado_nuevo]})

    except Exception as e:
        return respuesta_json_fail(str(e), 500)
