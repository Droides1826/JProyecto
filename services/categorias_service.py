from utils.baseDatos import BaseDatos
from utils.utils import respuesta_json_success, respuesta_json_fail

def obtener_categorias():
        db = BaseDatos()
        categorias = db.ejecutar_consulta("SELECT * FROM categorias")
        return categorias
    

def ingresar_categoria(valores_categoria):
        db = BaseDatos()
        query = "INSERT INTO categorias (nombre_categoria, descripcion) VALUES (%s, %s)"
        valores = (valores_categoria['nombre'], 
                    valores_categoria['descripcion']
                   )
        db.ejecutar_accion(query, valores)