from utils import Validaciones



def validaciones_ingresar_categorias(valores_categorias):
    if not valores_categorias["nombre"]:
        return "El nombre de la categoría no puede estar vacío."
    if Validaciones.es_solo_numeros(valores_categorias["nombre"]):
        return "El nombre de la categoría no puede ser solo números."
    if Validaciones.es_solo_numeros(valores_categorias["descripcion"]):
        return "La descripción de la categoría no puede ser solo números."
    if not Validaciones.es_solo_letras(valores_categorias["nombre"]):
        return "El nombre de la categoría solo puede contener letras."

    if Validaciones.tiene_caracteres_especiales(valores_categorias["nombre"]):
        return "El nombre de la categoría no puede contener caracteres especiales."

    if not Validaciones.limite_caracteres(valores_categorias["nombre"], 30):
        return "El nombre de la categoría no puede tener más de 30 caracteres."
    
    
    if not Validaciones.limite_caracteres(valores_categorias["descripcion"], 255):
        return "La descripción no puede tener más de 255 caracteres."
    return None
    



def validaciones_actualizar_categorias(valores_categorias):
    if not valores_categorias["nombre"] and not valores_categorias["descripcion"]:
        return "El ID y el nombre de la categoría son obligatorios."
    if not Validaciones.es_solo_numeros(valores_categorias["id_categoria"]):
        return "El ID de la categoría debe ser un número."
    if Validaciones.es_solo_numeros(valores_categorias["nombre"]):
        return "El nombre de la categoría no puede ser solo números."
    if Validaciones.es_solo_numeros(valores_categorias["descripcion"]):
        return "La descripción de la categoría no puede ser solo números."
    if valores_categorias["nombre"]:
        if not Validaciones.es_solo_letras(valores_categorias["nombre"]):
            return "El nombre solo puede contener letras."
        if Validaciones.tiene_caracteres_especiales(valores_categorias["nombre"]):
            return "El nombre no puede contener caracteres especiales."
        if not Validaciones.limite_caracteres(valores_categorias["nombre"], 30):
            return "El nombre no puede tener más de 30 caracteres."
        
    if valores_categorias["descripcion"]:
        if not Validaciones.limite_caracteres(valores_categorias["descripcion"], 255):
            return "La descripción no puede tener más de 255 caracteres."
    return None


def validaciones_cambiar_estado_categorias(valores_categorias):
    if not valores_categorias["id_categoria"] or not valores_categorias["estado"]:
        return "El ID y el estado de la categoría son obligatorios."
    if not Validaciones.es_solo_numeros(valores_categorias["id_categoria"]):
        return "El ID de la categoría debe ser un número."
    if Validaciones.es_solo_numeros(valores_categorias["estado"]):
        return "El estado de la categoría no puede ser solo números."
    return None