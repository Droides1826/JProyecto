from flask import Blueprint, request
from utils.respuestas import respuesta_json_success, respuesta_json_fail
from services.categorias_service import obtener_categorias, ingresar_categoria, actualizar_categoria, cambiar_estado_categoria	
from utils.Validaciones_categorias import validaciones_ingresar_categorias, validaciones_actualizar_categorias, validaciones_cambiar_estado_categorias



categorias = Blueprint("categorias", __name__)


@categorias.route("/categorias", methods=["GET"])
def get_categorias():
    try:
        categorias = obtener_categorias()
        return respuesta_json_success(categorias, 200)
    except Exception as e:
        return respuesta_json_fail(str(e))


@categorias.route("/ingresar_categorias", methods=["POST"])
def create_categoria():
    try:
        valores_categorias = {
            "nombre": request.json["nombre"],
            "descripcion": request.json["descripcion"],
        }
        validacion = validaciones_ingresar_categorias(valores_categorias)
        if validacion :
            return respuesta_json_fail(validaciones_ingresar_categorias(valores_categorias), 400)

        ingresar_categoria(valores_categorias)
        return respuesta_json_success(
            {"mensaje": "Categoría ingresada exitosamente"}, 200
        )

    except Exception as e:
        return respuesta_json_fail(str(e), 400)


@categorias.route("/actualizar_categorias", methods=["PUT"])
def actualizar_categorias():
    try:
        valores_categorias = {
            "id_categoria": request.json["id_categoria"],
            "nombre": request.json["nombre"],
            "descripcion": request.json["descripcion"],
        }
        validar_categoria= validaciones_actualizar_categorias(valores_categorias)
        if validar_categoria:
            return respuesta_json_fail(validaciones_actualizar_categorias(valores_categorias), 400)

        filas_afectadas = actualizar_categoria(valores_categorias)

        if filas_afectadas == 0:
            return respuesta_json_fail("No se encontró la categoría o no hubo cambios.", 404)
        if filas_afectadas == 1:
            return respuesta_json_fail("La categoría ya se encuentra con ese nombre", 200)
        
        return respuesta_json_success({"mensaje": "Categoría actualizada exitosamente"}, 200)

    except Exception as e:
        return respuesta_json_fail(str(e), 500)
    

@categorias.route("/cambiar_estado_categoria", methods=["POST"])
def cambiar_estado_categorias():
    try:
        datos = request.get_json()
        valores_categorias = {
            "id_categoria": datos.get("id_categoria"),
            "estado": datos.get("estado"),
        }
        validacion_estado= validaciones_cambiar_estado_categorias(valores_categorias)
        if validacion_estado:
            return respuesta_json_fail(validaciones_cambiar_estado_categorias(valores_categorias), 400)

        filas_afectadas = cambiar_estado_categoria(valores_categorias)

        if filas_afectadas == 0:
            return respuesta_json_fail("No se encontró la categoría o no hubo cambios.", 404)
        
        if filas_afectadas == 1:
            return respuesta_json_fail("La categoria ya se encuentra en ese estado", 200)
        
        if filas_afectadas == 2:
            return respuesta_json_fail("No se puede cambiar el estado de la categoría : no existe, Debe ser Activo o Inactivo ", 400)

        return respuesta_json_success({"mensaje": "Categoría actualizada exitosamente"}, 200)

    except Exception as e:
        return respuesta_json_fail(str(e), 500)


