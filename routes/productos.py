from flask import Blueprint, jsonify, request
from utils.respuestas import respuesta_json_success, respuesta_json_fail
from services.productos_services import  ingresar_producto, obtener_datos_producto, update_products, cambiar_estado_productos
from utils.Validaciones_productos import validaciones_ingresar_productos,actualizar_productos,cambiar_estado_productos
productos = Blueprint('productos', __name__)

@productos.route('/productos', methods=['GET'])
def obtener_producto():
    try:
        productos = obtener_datos_producto()
        return jsonify(productos)
    except Exception as e:
        return respuesta_json_fail(str(e))

@productos.route('/ingresar_producto', methods=['POST'])
def create_product():
    try:
        valores_productos = {
            'nombre': request.form['nombre'],
            'descripcion': request.form['descripcion'],
            'precio': request.form['precio'],
            'id_categoria': request.form['id_categoria'],
            'cantidad': request.form['cantidad'],
        }
        
        ingresar = validaciones_ingresar_productos(valores_productos)
        if ingresar:
            return respuesta_json_fail(ingresar, 400)


        respuesta=ingresar_producto(valores_productos)

        if respuesta == 0:
            return respuesta_json_fail("La categoria no existe", 400)
        return respuesta_json_success({'mensaje': 'Producto ingresado exitosamente'})
        
    except Exception as e:
        return respuesta_json_fail(str(e))



@productos.route('/actualizar_producto', methods=['PUT'])
def actualizar_producto():
    try:
        datos = request.json
        valores_producto = {
            'id_producto': str(datos.get('id_producto')),
            'nombre': str(datos.get('nombre', '')).strip(),
            'descripcion': str(datos.get('descripcion', '')).strip(),
            'precio': str(datos.get('precio', '')),
            'cantidad': str(datos.get('cantidad', '')),
        }

        actualizar = actualizar_productos(valores_producto)
        if actualizar:
            return respuesta_json_fail(actualizar, 400)
            
        valores_producto = {k: v for k, v in valores_producto.items() if v}
        filas_afectadas = update_products(valores_producto)

        if filas_afectadas == 0:
            return respuesta_json_fail("No se encontró el producto o no hubo cambios.", 404)

        return respuesta_json_success({"mensaje": "Producto actualizado exitosamente"}, 200)

    except Exception as e:
        return respuesta_json_fail(str(e), 500)



@productos.route('/cambiar_estado_producto', methods=['POST'])
def cambiar_estado_product():
    try:
        datos = request.get_json()
        
        if not datos:
            return respuesta_json_fail('No se enviaron datos para actualizar.', 400)

        valores_producto = {
            'id_producto': datos.get('id_producto'),
            'estado': datos.get('estado')
        }

        estado = cambiar_estado_productos(valores_producto)
        if estado:
            return respuesta_json_fail(estado, 400)
        
        

        filas_afectadas = cambiar_estado_productos(valores_producto)

        if filas_afectadas == 0:
            return respuesta_json_fail("No se encontró el producto o no hubo cambios.", 404)

        if filas_afectadas == 1:
            return respuesta_json_fail("El producto ya se encuentra en ese estado.", 200)

        if filas_afectadas == 2:
            return respuesta_json_fail("No se puede cambiar el estado del producto: el estado es inválido.", 400)

        return respuesta_json_success({"mensaje": "Estado del producto actualizado exitosamente"}, 200)

    except Exception as e:
        return respuesta_json_fail(str(e), 500)



