from utils import Validaciones


def validaciones_ingresar_productos(valores_productos):

    if not valores_productos["nombre"] or not valores_productos["precio"] or not valores_productos["cantidad"] or not valores_productos["id_categoria"]:
        return "El nombre,  el precio, el stock y la categoría son obligatorios."
    
    if not Validaciones.limite_caracteres(valores_productos["nombre"], 30):
        return "El nombre del producto debe contener solo letras y no caracteres especiales y un limite de 30 caracteres."
    
    if not Validaciones.limite_caracteres(valores_productos["descripcion"], 255):
        return "La descripción no puede tener más de 255 caracteres."
    
    if not Validaciones.validacion_de_precio(valores_productos["precio"]):
        return "El precio debe ser un número entero y sin caracteres especiales y un limite de 10 numeros"
    
    if "." in valores_productos['precio'] or "," in valores_productos['precio']:
        return ('El precio debe contener solo números, sin puntos ni comas ni letras')
    
    if not Validaciones.validacion_de_id_categoria(valores_productos["id_categoria"]):
        return "El ID de la categoría debe ser un número válido y sin caracteres especiales."
        
    if not Validaciones.es_solo_numeros(valores_productos["cantidad"]):
        return "El stock debe ser un número entero."
    
    if not Validaciones.validacion_de_cantidad(valores_productos["cantidad"]):
        return "La cantidad debe ser un número válido < 10000 y sin caracteres especiales."
    
    if not Validaciones.es_solo_letras(valores_productos["nombre"]):
        return "El nombre solo puede contener letras."
    return None



def actualizar_productos(valores_productos):
    if not valores_productos['id_producto']:
        return "El ID del producto es obligatorio."
    
    if 'nombre' in valores_productos and valores_productos['nombre']:
        v_nombre=Validaciones.validacion_nombre(valores_productos['nombre'])
        if v_nombre is not True:
            return "El nombre del producto debe contener solo letras y no caracteres especiales y un limite de 30 caracteres."
    
    if 'precio' in valores_productos and valores_productos['precio']:
        v_precio = Validaciones.validacion_precio(valores_productos['precio'])
        if v_precio is not True:
            return "El precio debe ser un número entero y sin caracteres especiales y un limite de 10 numeros"
    
    if valores_productos["descripcion"]:
        if not Validaciones.limite_caracteres(valores_productos["descripcion"], 255):
            return "La descripción no puede tener más de 255 caracteres."
        if not Validaciones.validacion_descripcion(valores_productos["descripcion"]):
            return "La descripción no puede tener caracteres especiales,iniciar con un numero U ser solo numeros."
    
    if valores_productos['cantidad']:
        v_cantidad = Validaciones.validacion_de_cantidad(valores_productos['cantidad'])
        if v_cantidad is not True:
            return "La cantidad debe ser un número válido < 10000 y sin caracteres especiales ."
    
    return None


def cambiar_estado_productos(valores_productos):
    if not valores_productos['id_producto'] or not valores_productos['estado']:
        return "El ID del producto y el estado son obligatorios."
    1
    if not Validaciones.es_solo_numeros(valores_productos['id_producto']):
        return "El ID del producto debe ser un número."
    
    if not Validaciones.es_solo_numeros(valores_productos['estado']):
        return "El estado del producto debe ser solo letras."
    
    if not valores_productos['estado'].lower() in ["activo", "inactivo"]:
        return "El estado del producto debe ser 'Activo' o 'Inactivo'."
    
    return None