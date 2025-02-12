from flask import Blueprint, request
from utils.respuestas import respuesta_json_success, respuesta_json_fail
from services.categorias_service import obtener_categorias, ingresar_categoria, actualizar_categoria, cambiar_estado_categoria	
from utils.Validaciones import es_solo_numeros,es_solo_letras,tiene_caracteres_especiales,limite_caracteres



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
        if not valores_categorias["nombre"]:
            return respuesta_json_fail(
                "El nombre de la categoría no puede estar vacío.", 400
            )
        if es_solo_numeros(valores_categorias["nombre"]):
            return respuesta_json_fail(
                "El nombre de la categoría no puede ser solo números.", 400
            )
        if es_solo_numeros(valores_categorias["descripcion"]):
            return respuesta_json_fail(
                "La descripción de la categoría no puede ser solo números.", 400
            )
        if not es_solo_letras(valores_categorias["nombre"]):
            return respuesta_json_fail(
                "El nombre de la categoría solo puede contener letras.", 400
            )

        if tiene_caracteres_especiales(valores_categorias["nombre"]):
            return respuesta_json_fail(
                "El nombre de la categoría no puede contener caracteres especiales.",
                400,
            )

        if not limite_caracteres(valores_categorias["nombre"], 30):
            return respuesta_json_fail(
                "El nombre de la categoría no puede tener más de 30 caracteres.", 400
            )
        
        
        if not limite_caracteres(valores_categorias["descripcion"], 255):
            return respuesta_json_fail(
                "La descripción no puede tener más de 255 caracteres.", 400
            )

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

        if not valores_categorias["nombre"] and not valores_categorias["descripcion"]:
            return respuesta_json_fail("El ID y el nombre de la categoría son obligatorios.", 400)
        
        if not es_solo_numeros(valores_categorias["id_categoria"]):
            return respuesta_json_fail("El ID de la categoría debe ser un número.", 400)
        if es_solo_numeros(valores_categorias["nombre"]):
            return respuesta_json_fail("El nombre de la categoría no puede ser solo números.", 400)
        if es_solo_numeros(valores_categorias["descripcion"]):
            return respuesta_json_fail("La descripción de la categoría no puede ser solo números.", 400)
        if valores_categorias["nombre"]:
            if not es_solo_letras(valores_categorias["nombre"]):
                return respuesta_json_fail("El nombre solo puede contener letras.", 400)
            if tiene_caracteres_especiales(valores_categorias["nombre"]):
                return respuesta_json_fail("El nombre no puede contener caracteres especiales.", 400)
            if not limite_caracteres(valores_categorias["nombre"], 30):
                return respuesta_json_fail("El nombre no puede tener más de 30 caracteres.", 400)
            
        if valores_categorias["descripcion"]:
            if not limite_caracteres(valores_categorias["descripcion"], 255):
                return respuesta_json_fail("La descripción no puede tener más de 255 caracteres.", 400)

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
        if not datos:
            return respuesta_json_fail("No se enviaron datos para actualizar.", 400)

        valores_categorias = {
            "id_categoria": datos.get("id_categoria"),
            "estado": datos.get("estado"),
        }
        if es_solo_numeros(valores_categorias["estado"]):
            return respuesta_json_fail("El estado de la categoria solo puede contener letras.", 400)

        if not es_solo_numeros(valores_categorias["id_categoria"]):
            return respuesta_json_fail("El id de la categoria solo puede contener numeros.", 400)

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


