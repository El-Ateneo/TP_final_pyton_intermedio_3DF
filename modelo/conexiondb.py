import sqlite3

class ConexionDB:
    def __init__(self):
        self.db_path = 'ddbb/biblioteca.db'
        self.conexion = sqlite3.connect(self.db_path)
        self.cursor = self.conexion.cursor()

    def cerrar_conexion(self):
        self.conexion.commit()
        self.conexion.close()