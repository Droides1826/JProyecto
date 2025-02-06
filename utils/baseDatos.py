from utils.db import conexion
from flask_mysqldb import MySQL

class BaseDatos:
    def __init__(self, app_or_connection=None):
        if app_or_connection:
            self.mysql = MySQL(app_or_connection)
        else:
            self.mysql = conexion
    
    def conectar(self):
        return self.mysql.connection.cursor()

    def ejecutar_consulta(self, query, valores=None, commit=False):
        cursor = self.conectar()
        cursor.execute(query, valores)
        resultado = cursor.fetchall()
        if commit:
            self.mysql.connection.commit()
        cursor.close()
        return resultado

    def ejecutar_accion(self, query, valores):
        cursor = self.conectar()
        cursor.execute(query, valores)
        self.mysql.connection.commit()
        cursor.close()

    def verificar_existencia(self, query, valores=None):
        cursor = self.conectar()
        cursor.execute(query, valores)
        existe = cursor.fetchone()
        cursor.close()
        return existe is not None
    

