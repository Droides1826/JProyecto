from flask import Blueprint, request, render_template
from utils.respuestas import respuesta_json_success, respuesta_json_fail
from services.categorias_service import obtener_categorias, ingresar_categoria
from utils.Validaciones import (es_solo_letras,tiene_caracteres_especiales,limite_caracteres
)


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


@categorias.route("/index")
def index():
    return render_template("index.html")
