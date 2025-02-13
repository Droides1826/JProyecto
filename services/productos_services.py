from utils.baseDatos import BaseDatos
from utils.respuestas import  respuesta_json_fail, respuesta_json_success


def obtener_datos_producto():
    db = BaseDatos()
    query = """
    SELECT p.id_producto, p.nombre, p.descripcion, p.precio, c.nombre_categoria AS categoria, p.cantidad, p.estado 
    FROM productos p
    JOIN categorias c ON p.id_categoria = c.id_categoria
    WHERE p.estado = 1
    """
    productos = db.ejecutar_consulta(query)
    
    productos_ = [
        {
            "id_producto": producto[0],
            "nombre": producto[1],
            "descripcion": producto[2],
            "precio": producto[3],
            "categoria": producto[4],
            "cantidad": producto[5],
            "estado": "activo" if producto[6] == 1 else None
        }
        for producto in productos
    ]
    return productos_

def ingresar_producto(valores_producto):
    
    try:
        db = BaseDatos()
        query = "INSERT INTO productos (nombre, descripcion, precio, id_categoria, cantidad) VALUES (%s, %s, %s, %s, %s)"
        

        valores= (
            valores_producto['nombre'],
            valores_producto['descripcion'],
            valores_producto['precio'],
            valores_producto['id_categoria'],
            valores_producto['cantidad'],

            )
        existe = db.ejecutar_consulta("SELECT estado FROM categorias WHERE id_categoria = %s", (valores_producto['id_categoria'],))
        if not existe:
            return 0
    
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
        product = db.ejecutar_consulta("SELECT nombre FROM productos WHERE id_producto = %s", (valores_producto['id_producto'],))
        
        if not product:
            return 0

        if 'nombre' in valores_producto:
            campos.append("nombre = %s")
            valores.append(valores_producto['nombre'])

        if 'descripcion' in valores_producto:
            campos.append("descripcion = %s")
            valores.append(valores_producto['descripcion'])

        if 'precio' in valores_producto:
            campos.append("precio = %s")
            valores.append(valores_producto['precio'])

        if 'cantidad' in valores_producto:
            campos.append("cantidad = %s")
            valores.append(valores_producto['cantidad'])

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
    
    lower_estado = estado.lower()
    
    valor_antiguo = db.ejecutar_consulta("SELECT estado FROM productos WHERE id_producto = %s", (id_producto,))
    if not valor_antiguo:
        return 0
    if lower_estado == 'activo':
        estado = 1
    if lower_estado == 'inactivo':
        estado = 2
    if estado == valor_antiguo[0][0]:
        return 1
    
    query = "UPDATE productos SET estado = %s WHERE id_producto = %s"
    valores = (estado, id_producto)
    return db.ejecutar_accion(query, valores)





