
import re

def es_solo_numeros(valor: str) -> bool:
    """Verifica si el valor contiene solo números."""
    return valor.isdigit()

def tiene_caracteres_especiales(valor: str) -> bool:
    """Verifica si el valor contiene caracteres especiales."""
    return bool(re.search(r"[^a-zA-Z0-9 ]", valor))

def limite_caracteres(valor: str, max_length: int) -> bool:
    """Verifica si el valor supera el límite de caracteres."""
    return len(valor) <= max_length

def es_solo_letras(valor: str) -> bool:
    """Verifica si el valor contiene solo letras."""
    return valor.replace(" ","").isalpha()

def es_correo_valido(correo: str) -> bool:
    """Verifica si el formato del correo es válido."""
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(patron, correo))

def longitud_valida(valor: str, min_length: int, max_length: int) -> bool:
    """Verifica si la longitud del valor está dentro de un rango válido."""
    return min_length <= len(valor) <= max_length

def es_numero_decimal(valor: str) -> bool:
    """Verifica si el valor es un número decimal válido."""
    return bool(re.match(r'^\d+(\.,\d+)?$', valor))

def es_fecha_valida(fecha: str) -> bool:
    """Verifica si el valor es una fecha en formato YYYY-MM-DD."""
    return bool(re.match(r'^\d{4}-\d{2}-\d{2}$', fecha))

def es_telefono_valido(telefono: str) -> bool:
    """Verifica si el número de teléfono tiene un formato válido (10 dígitos)."""
    return bool(re.match(r'^\d{10}$', telefono))

def es_contrasena_segura(contrasena: str) -> bool:
    """Verifica si la contraseña es segura (mínimo 8 caracteres, una mayúscula, una minúscula y un número)."""
    patron = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$'
    return bool(re.match(patron, contrasena))

def es_solo_numeros(valor) -> bool:
    """Verifica si el valor contiene solo números."""
    return str(valor).isdigit()


def validacion_de_nombre(nombre: str) -> bool:
    if not nombre:
        print("El nombre del producto es obligatorio.")
        return False
    if not es_solo_letras(nombre):
        print("El nombre del producto debe contener solo letras y no caracteres especiales.")
        return False
        
    if tiene_caracteres_especiales(nombre):
        print("El nombre del producto no puede contener caracteres especiales.")
        return False
    if not limite_caracteres(nombre, 30):
        print("El nombre del producto no puede tener más de 30 caracteres.")
        return False
    return True

def validacion_nombre(nombre: str) -> bool:  
    if not nombre:
        print("El nombre del producto es obligatorio.")
        return False
    if not limite_caracteres(nombre, 30):
        print("El nombre del producto no puede tener más de 30 caracteres.")
        return False
    if es_solo_numeros(nombre):
        print("El nombre del producto no puede ser solo números.")
        return False
    return True

def validacion_de_precio(precio: str) -> bool:
    if not precio:
        return False
    if not es_numero_decimal(precio):
        return False
    if not limite_caracteres(precio, 10):
        return False
    return True

def validacion_precio(precio: str) -> bool:
    if not limite_caracteres(precio, 10):
        return False
    if not es_solo_numeros(precio):
        return False
    return True

def validacion_de_cantidad(cantidad: str) -> bool:
    if not cantidad:
        return False
    if not es_solo_numeros(cantidad):
        return False
    return True

def validacion_de_id_categoria(id_categoria: str) -> bool:
    if not id_categoria:
        return False
    if not es_solo_numeros(id_categoria):
        return False
    return True

def validacion_de_cantidad(cantidad: str) -> bool:
    if not cantidad:
        return False
    if not es_solo_numeros(cantidad):
        return False
    if not limite_caracteres(cantidad, 4):
        return False
    return True



def validacion_descripcion(descripcion: str) -> bool:
    if not descripcion:
        return True
    if not limite_caracteres(descripcion, 255):
        return False
    if es_solo_numeros(descripcion):
        return False
    return True