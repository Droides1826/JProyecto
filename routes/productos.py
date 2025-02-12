from flask import Blueprint, jsonify, request
from utils.respuestas import respuesta_json_success, respuesta_json_fail
from services.productos_services import  ingresar_producto, obtener_datos_producto, update_products, cambiar_estado_productos
from utils.Validaciones import es_solo_numeros,validacion_de_nombre, validacion_de_cantidad,validacion_de_precio ,validacion_de_nombre,validacion_de_id_categoria

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
        }
        if "." in valores_producto['precio'] or "," in valores_producto['precio']:
            return respuesta_json_fail('El precio debe contener solo números, sin puntos ni comas ni letras', 400)

        validacion_nombre = validacion_de_nombre(valores_producto['nombre'])
        if validacion_nombre is not True:
            return validacion_nombre
        
        validacion_precio = validacion_de_precio(valores_producto['precio'])
        if validacion_precio is not True:
            return validacion_precio
        
        validacion_cantidad = validacion_de_cantidad(valores_producto['cantidad'])
        if validacion_cantidad is not True:
            return validacion_cantidad
        
        validacion_id_categorias = validacion_de_id_categoria(valores_producto['id_categoria'])
        if validacion_id_categorias is not True:
            return validacion_id_categorias
        
        respuesta=ingresar_producto(valores_producto)
        if respuesta == 0:
            return respuesta_json_fail("La categoria no existe", 400)
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
            'id_producto': str(datos.get('id_producto')),
            'nombre': str(datos.get('nombre', '')).strip(),
            'descripcion': str(datos.get('descripcion', '')).strip(),
            'precio': str(datos.get('precio', '')),
            'cantidad': str(datos.get('cantidad', '')),
        }
        if not valores_producto['id_producto']:
            return respuesta_json_fail("El ID del producto es obligatorio.", 400)
        
        if not validacion_de_nombre(valores_producto['nombre']):
            return respuesta_json_fail("El nombre del producto solo puede contener letras.", 400)
        
        if not validacion_de_precio(valores_producto['precio']):
            return respuesta_json_fail("El precio debe ser un número válido sin caracteres especiales.", 400)

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

        # Validaciones
        if not es_solo_numeros(valores_producto['id_producto']):
            return respuesta_json_fail("El ID del producto debe contener solo números.", 400)

        if valores_producto['estado'] not in ["Activo", "Inactivo"]:
            return respuesta_json_fail("El estado del producto debe ser 'Activo' o 'Inactivo'.", 400)

        # Intentar cambiar el estado del producto
        filas_afectadas = cambiar_estado_productos(valores_producto)

        if filas_afectadas == 0:
            return respuesta_json_fail("No se encontró el producto o no hubo cambios.", 404)

        if filas_afectadas == 1:
            return respuesta_json_fail("El producto ya se encuentra en ese estado.", 200)

        if filas_afectadas == 2:
            return respuesta_json_fail("No se puede cambiar el estado del producto: no existe o el estado es inválido.", 400)

        return respuesta_json_success({"mensaje": "Estado del producto actualizado exitosamente"}, 200)

    except Exception as e:
        return respuesta_json_fail(str(e), 500)



