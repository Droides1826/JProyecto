from flask import Blueprint, jsonify, request
from utils.respuestas import respuesta_json_success, respuesta_json_fail
from services.productos_services import  ingresar_producto, obtener_datos_producto, update_products, cambiar_estado_productos
from utils.Validaciones import validacion_de_nombre, validacion_de_cantidad,validacion_de_precio ,validacion_de_nombre,validacion_de_id_categoria

productos = Blueprint('productos', __name__)


@productos.route('/ingresar_producto', methods=['POST'])
def create_product():
    try:
        valores_producto = {
            'nombre': request.form['nombre'],
            'descripcion': request.form['descripcion'],
            'precio': request.form['precio'],
            'id_categoria': request.form['id_categoria'],
            'cantidad': request.form['cantidad'],
            'imagen': request.files['imagen'].read() if 'imagen' in request.files else None
        }
        
        validacion_nombre = validacion_de_nombre(valores_producto['nombre'])
        if validacion_nombre is not True:
            return validacion_nombre
        
        
        validacion_cantidad = validacion_de_cantidad(valores_producto['cantidad'])
        if validacion_cantidad is not True:
            return validacion_cantidad
        
        validacion_id_categorias = validacion_de_id_categoria(valores_producto['id_categoria'])
        if validacion_id_categorias is not True:
            return validacion_id_categorias
            
        ingresar_producto(valores_producto)
        return respuesta_json_success({'mensaje': 'Producto ingresado exitosamente'})
        
    except Exception as e:
        return respuesta_json_fail(str(e))


@productos.route('/productos', methods=['GET'])
def obtener_producto():
    try:
        productos = obtener_datos_producto()
        return jsonify(productos)
    except Exception as e:
        return respuesta_json_fail(str(e))

@productos.route('/actualizar_producto', methods=['PUT'])
def actualizar_producto():
    try:
        datos = request.json
        valores_producto = {
            'id_producto': datos.get('id_producto'),
            'nombre': datos.get('nombre', '').strip(),
            'descripcion': datos.get('descripcion', '').strip(),
            'precio': datos.get('precio'),
            'id_categoria': datos.get('id_categoria' ),
            'cantidad': datos.get('cantidad'),
        }

        if validacion_de_precio(valores_producto['precio']):
            return respuesta_json_fail('El precio debe contener solo numeros.', 400)

        valores_producto = {k: v for k, v in valores_producto.items() if v not in [None, '', ' ']}

        if 'id_producto' not in valores_producto:
            return respuesta_json_fail("El ID del producto es obligatorio.", 400)
        

        filas_afectadas = update_products(valores_producto)

        if filas_afectadas == 0:
            return respuesta_json_fail("No se encontró el producto o no hubo cambios.", 404)

        return respuesta_json_success({'mensaje': 'Producto actualizado exitosamente'}, 200)
    
    except Exception as e:
        return respuesta_json_fail(str(e), 500)


@productos.route('/cambiar_estado_producto', methods=['POST'])
def cambiar_estado_product():
    try:
        datos = request.get_json()
        if not datos:
            return respuesta_json_fail('No se enviaron datos para actualizar.', 400)
        
        valores_producto = {
            'id_producto': datos['id_producto'],
            'estado': datos['estado']
        }
        
        filas_afectadas = cambiar_estado_productos(valores_producto)
        
        if filas_afectadas == 0:
            return respuesta_json_fail("No se encontró la categoría o no hubo cambios.", 404)
        
        if filas_afectadas == 1:
            return respuesta_json_fail("La categoria ya se encuentra en ese estado", 200)
        
        if filas_afectadas == 2:
            return respuesta_json_fail("No se puede cambiar el estado de la categoría : no existe, Debe ser Activo o Inactivo ", 400)

        return respuesta_json_success({"mensaje": "Categoría actualizada exitosamente"}, 200)

    
    except Exception as e:
        return respuesta_json_fail(str(e), 500)


