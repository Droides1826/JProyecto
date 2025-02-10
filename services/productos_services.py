import base64
from utils.baseDatos import BaseDatos
from utils.respuestas import  respuesta_json_fail, respuesta_json_success

activo = 1
inactivo = 2

def convertir_imagen_base64(imagen_blob):
    return base64.b64encode(imagen_blob).decode('utf-8')

def obtener_datos_producto():
    db = BaseDatos()
    cursor = db.conectar()
    query = "SELECT id_producto, nombre, descripcion, precio, id_categoria, cantidad, imagen FROM productos WHERE estado = 1"
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
        query = "UPDATE productos SET "
        valores = []
        campos = []

        if 'nombre' in valores_producto:
            campos.append("nombre = %s")
            valores.append(valores_producto['nombre'])

        if 'descripcion' in valores_producto:
            campos.append("descripcion = %s")
            valores.append(valores_producto['descripcion'])

        if 'precio' in valores_producto:
            campos.append("precio = %s")
            valores.append(valores_producto['precio'])

        if 'id_categoria' in valores_producto:
            campos.append("id_categoria = %s")
            valores.append(valores_producto['id_categoria'])

        if 'cantidad' in valores_producto:
            campos.append("cantidad = %s")
            valores.append(valores_producto['cantidad'])

        if 'imagen' in valores_producto:
            campos.append("imagen = %s")
            valores.append(valores_producto['imagen'])

        if not campos:
            return 0  

        query += ", ".join(campos) + " WHERE id_producto = %s"
        valores.append(valores_producto['id_producto'])

        return db.ejecutar_accion(query, valores)
    
    except Exception as e:
        return respuesta_json_fail(str(e), 500)



def cambiar_estado_productos(Valores_productos):
    db = BaseDatos()
    id_producto = Valores_productos["id_producto"]
    estado = Valores_productos["estado"]
    
    producto = db.ejecutar_consulta("SELECT * FROM productos WHERE id_producto = %s", (id_producto,))
    if not producto:
        return 0 
    
    query = "UPDATE productos SET estado = %s WHERE id_producto = %s"
    valores = (estado, id_producto)
    return db.ejecutar_accion(query, valores)
