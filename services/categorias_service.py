from utils.baseDatos import BaseDatos

activo = 1
inactivo = 2
def obtener_categorias():
        db = BaseDatos()
        categorias = db.ejecutar_consulta("SELECT * FROM categorias WHERE estado = 1")
        return categorias
    

def ingresar_categoria(valores_categorias):
        db = BaseDatos()
        query = "INSERT INTO categorias (nombre_categoria, descripcion) VALUES (%s, %s)"
        valores = (valores_categorias['nombre'], 
                    valores_categorias['descripcion'])        
        db.ejecutar_accion(query,valores)

def actualizar_categoria(valores_categorias):
    db = BaseDatos()
    query = "UPDATE categorias SET "
    valores = []
    campos = []

    if valores_categorias["nombre"]:
        campos.append("nombre_categoria = %s")
        valores.append(valores_categorias["nombre"])

    if valores_categorias["descripcion"]:
        campos.append("descripcion = %s")
        valores.append(valores_categorias["descripcion"])

    if not campos:
        return 0  

    query += ", ".join(campos) + " WHERE id_categoria = %s"
    valores.append(valores_categorias["id_categoria"])

    return db.ejecutar_accion(query, valores)

def cambiar_estado_categoria(Valores_categorias):
        db = BaseDatos()
        id_categoria = Valores_categorias["id_categoria"]
        estado = Valores_categorias["estado"]
        
        categoria = db.ejecutar_consulta("SELECT * FROM categorias WHERE id_categoria = %s", (id_categoria,))
        if not categoria:
                return 0 
        
        query = "UPDATE categorias SET estado = %s WHERE id_categoria = %s"
        valores = (estado, id_categoria)
        return db.ejecutar_accion(query, valores)
