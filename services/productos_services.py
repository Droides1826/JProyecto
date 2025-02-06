import base64
from utils.baseDatos import BaseDatos
from utils.respuestas import  respuesta_json_fail, respuesta_json_success

def convertir_imagen_base64(imagen_blob):
    return base64.b64encode(imagen_blob).decode('utf-8')

def obtener_datos_producto():
    db = BaseDatos()
    cursor = db.conectar()
    query = "SELECT id_producto, nombre, descripcion, precio, id_categoria, cantidad, imagen FROM productos"
    cursor.execute(query)
    resultados = cursor.fetchall()
    cursor.close()
    
    productos = []
    for resultado in resultados:
        producto = {
            'id_producto': resultado[0],
            'nombre': resultado[1],
            'descripcion': resultado[2],
            'precio': resultado[3],
            'id_categoria': resultado[4],
            'cantidad': resultado[5],
            'imagen': resultado[6]
        }
        productos.append(producto)
    
    return productos

def ingresar_producto(valores_producto):
    try:
        db = BaseDatos()
        query = "INSERT INTO productos (nombre, descripcion, precio, id_categoria, cantidad, imagen) VALUES (%s, %s, %s, %s, %s, %s)"
        valores= (
            valores_producto['nombre'],
            valores_producto['descripcion'],
            valores_producto['precio'],
            valores_producto['id_categoria'],
            valores_producto['cantidad'],
            valores_producto['imagen']
            )
        db.ejecutar_accion(query, valores)
        return  respuesta_json_success ({'mensaje': 'Producto ingresado exitosamente'})
    except Exception as e:
        return respuesta_json_fail(str(e))

def update_products(valores_producto):
    try:
        db = BaseDatos()
        query = "UPDATE productos SET nombre = %s, descripcion = %s, precio = %s, id_categoria = %s, cantidad = %s, imagen = %s WHERE id_producto = %s"
        valores = (
            valores_producto['nombre'],
            valores_producto['descripcion'],
            valores_producto['precio'],
            valores_producto['id_categoria'],
            valores_producto['cantidad'],
            valores_producto['imagen'],
            valores_producto['id_producto']
        )
        db.ejecutar_accion(query, valores)
    except Exception as e:
        return respuesta_json_fail(str(e))



