from flask import Blueprint, jsonify, request, redirect, url_for, render_template
from utils.utils import respuesta_json_success, respuesta_json_fail
from services.productos_services import  ingresar_producto, obtener_datos_producto, convertir_imagen_base64, update_products

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
        
        ingresar_producto(valores_producto)
        return respuesta_json_success({'mensaje': 'Producto ingresado exitosamente'})
        
    except Exception as e:
        return respuesta_json_fail(str(e))

@productos.route('/productos', methods=['GET'])
def obtener_producto():
    try:
        productos = obtener_datos_producto()
        
        # Convertir las imágenes BLOB en base64 para el frontend
        for producto in productos:
            if producto['imagen']:
                producto['imagen'] = convertir_imagen_base64(producto['imagen'])
        
        return jsonify(productos)
    except Exception as e:
        return respuesta_json_fail(str(e))

@productos.route('/actualizar_producto', methods=['POST'])
def actualizar_producto():
    try:
        valores_producto = {
            'nombre': request.form['nombre'],
            'descripcion': request.form['descripcion'],
            'precio': request.form['precio'],
            'id_categoria': request.form['id_categoria'],
            'cantidad': request.form['cantidad'],
            'imagen': request.files['imagen'].read() if 'imagen' in request.files else None,
            'id_producto': request.form['id_producto']
        }
        update_products(valores_producto)
        return respuesta_json_success({'mensaje': 'Producto actualizado exitosamente'})
    except Exception as e:
        return respuesta_json_fail(str(e))


