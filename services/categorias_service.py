from utils.baseDatos import BaseDatos


def obtener_categorias():
    db = BaseDatos()
    cursor = db.conectar()
    query = "SELECT * FROM categorias WHERE estado = 1"
    cursor.execute(query)
    resultados = cursor.fetchall()
    cursor.close()

    categorias = []
    for resultado in resultados:
        categoria = {
            'id_categoria': resultado[0],
            'nombre_categoria': resultado[1],
            'descripcion': resultado[2],
            'estado': 'activo' if resultado[3] == 1 else None
        }
        categorias.append(categoria)

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
    existe = db.ejecutar_consulta("SELECT 1 FROM categorias WHERE id_categoria = %s AND nombre_categoria = %s",(valores_categorias['id_categoria'], valores_categorias['nombre']))
    valor = db.ejecutar_consulta("SELECT * FROM categorias WHERE id_categoria = %s", (valores_categorias['id_categoria'],))
    if not valor:
        return 0
    if existe:
        return 1
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
    lower_estado = estado.lower()
    if lower_estado not in ['activo', 'inactivo']:
        return 2
    if lower_estado == 'activo':
        estado = 1
    if lower_estado == 'inactivo':
        estado = 2
    valor_antiguo = db.ejecutar_consulta("SELECT estado FROM categorias WHERE id_categoria = %s", (id_categoria,))
    
    if not valor_antiguo:
        return 0
    
    if estado== valor_antiguo[0][0]:
        return 1
    query = "UPDATE categorias SET estado = %s WHERE id_categoria = %s"
    valores = (estado, id_categoria)
    return db.ejecutar_accion(query, valores)
