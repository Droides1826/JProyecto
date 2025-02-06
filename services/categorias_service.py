from utils.baseDatos import BaseDatos
from utils.respuestas import respuesta_json_success, respuesta_json_fail

def obtener_categorias():
        db = BaseDatos()
        categorias = db.ejecutar_consulta("SELECT * FROM categorias")
        return categorias
    

def ingresar_categoria(valores_categorias):
        db = BaseDatos()
        query = "INSERT INTO categorias (nombre_categoria, descripcion) VALUES (%s, %s)"
        valores = (valores_categorias['nombre'], 
                    valores_categorias['descripcion'])
        print("Insertando categoría:", valores_categorias)
        
        db.ejecutar_accion(query,valores)