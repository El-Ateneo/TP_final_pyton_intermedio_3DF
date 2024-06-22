from .conexiondb import ConexionDB

def crear_tablas():
    conn = ConexionDB()
    
    # Crear tabla Genero
    sql_genero = '''
        CREATE TABLE IF NOT EXISTS Genero(
            ID INTEGER PRIMARY KEY AUTOINCREMENT, 
            Nombre VARCHAR(50) NOT NULL
        )
    '''
    
    # Crear tabla Editorial
    sql_editorial = '''
        CREATE TABLE IF NOT EXISTS Editorial(
            ID INTEGER PRIMARY KEY AUTOINCREMENT, 
            Nombre VARCHAR(100) NOT NULL
        )
    '''
    
    # Crear tabla Libros
    sql_libros = '''
        CREATE TABLE IF NOT EXISTS Libros(
            ID INTEGER PRIMARY KEY AUTOINCREMENT, 
            Titulo VARCHAR(150) NOT NULL,
            Autor VARCHAR(100) NOT NULL,
            Genero INTEGER,
            Editorial INTEGER,
            Ano INTEGER,
            ISBN VARCHAR(13),
            FOREIGN KEY (Genero) REFERENCES Genero(ID),
            FOREIGN KEY (Editorial) REFERENCES Editorial(ID)
        )
    '''
    
    try:
        conn.cursor.execute(sql_genero)
        conn.cursor.execute(sql_editorial)
        conn.cursor.execute(sql_libros)
        conn.conexion.commit()
        conn.cerrar_conexion()
        print("Tablas creadas exitosamente.")
    except Exception as e:
        print(f"Error al crear las tablas: {e}")

def listar_generos():
    conn = ConexionDB()
    generos = []
    sql = """
            SELECT * FROM Genero
            """
    
    try:
        conn.cursor.execute(sql)
        generos = conn.cursor.fetchall()
        conn.cerrar_conexion()
        return generos
    except Exception as e:
        print(f"Error al listar los géneros: {e}")
        return []

def listar_editoriales():
    conn = ConexionDB()
    editoriales = []
    sql = """
            SELECT * FROM Editorial
        """
    
    try:
        conn.cursor.execute(sql)
        editoriales = conn.cursor.fetchall()
        conn.cerrar_conexion()
        return editoriales
    except Exception as e:
        print(f"Error al listar las editoriales: {e}")
        return []

def listar_libros():
    conn = ConexionDB()
    libros = []
    try: 
        sql = """
                SELECT
                    Libros.ID,
                    Libros.Titulo,
                    Libros.Autor,
                    Genero.Nombre AS Genero,
                    Editorial.Nombre AS Editorial,
                    Libros.Ano,
                    Libros.ISBN
                FROM
                    Libros
                LEFT JOIN
                    Genero ON Libros.Genero = Genero.ID
                LEFT JOIN
                    Editorial ON Libros.Editorial = Editorial.ID
            """
    
    
        conn.cursor.execute(sql)
        libros = conn.cursor.fetchall()
        conn.cerrar_conexion()
        return libros
    except Exception as e:
        print(f"Error al listar los libros: {e}")
        return []

class Libros:
    def __init__(self, titulo, autor, genero, editorial, ano, isbn):
        self.id_libros = None
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.editorial = editorial
        self.ano = ano
        self.isbn = isbn
    
    def __str__(self):
        return f'Libro[{self.titulo},{self.autor},{ self.genero},{self.editorial},{self.ano},{self.isbn}]'


def guardar_libro(libro):
    conn = ConexionDB()

    try:
        # Verificar si el género ya existe
        conn.cursor.execute("SELECT ID FROM Genero WHERE Nombre = ?", (libro.genero,))
        genero_id = conn.cursor.fetchone()
        if not genero_id:
            conn.cursor.execute("INSERT INTO Genero (Nombre) VALUES (?)", (libro.genero,))
            genero_id = conn.cursor.lastrowid
        else:
            genero_id = genero_id[0]

        # Verificar si la editorial ya existe
        conn.cursor.execute("SELECT ID FROM Editorial WHERE Nombre = ?", (libro.editorial,))
        editorial_id = conn.cursor.fetchone()
        if not editorial_id:
            conn.cursor.execute("INSERT INTO Editorial (Nombre) VALUES (?)", (libro.editorial,))
            editorial_id = conn.cursor.lastrowid
        else:
            editorial_id = editorial_id[0]

        # Guardar el libro
        conn.cursor.execute("""
            INSERT INTO Libros (Titulo, Autor, Genero, Editorial, Ano, ISBN)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (libro.titulo, libro.autor, genero_id, editorial_id, libro.ano, libro.isbn))
        
        conn.cerrar_conexion()
    except Exception as e:
        print(f"Error al guardar el libro: {e}")
        conn.cerrar_conexion()

def editar_libro(libro, id_libro):
    conn = ConexionDB()

    try:
        # Verificar si el género ya existe
        conn.cursor.execute("SELECT ID FROM Genero WHERE Nombre = ?", (libro.genero,))
        genero_id = conn.cursor.fetchone()
        if not genero_id:
            conn.cursor.execute("INSERT INTO Genero (Nombre) VALUES (?)", (libro.genero,))
            genero_id = conn.cursor.lastrowid
        else:
            genero_id = genero_id[0]

        # Verificar si la editorial ya existe
        conn.cursor.execute("SELECT ID FROM Editorial WHERE Nombre = ?", (libro.editorial,))
        editorial_id = conn.cursor.fetchone()
        if not editorial_id:
            conn.cursor.execute("INSERT INTO Editorial (Nombre) VALUES (?)", (libro.editorial,))
            editorial_id = conn.cursor.lastrowid
        else:
            editorial_id = editorial_id[0]

        # Actualizar el libro
        conn.cursor.execute("""
            UPDATE Libros
            SET Titulo = ?, Autor = ?, Genero = ?, Editorial = ?, Ano = ?, ISBN = ?
            WHERE ID = ?
        """, (libro.titulo, libro.autor, genero_id, editorial_id, libro.ano, libro.isbn, id_libro))
        
        conn.cerrar_conexion()
    except Exception as e:
        print(f"Error al editar el libro: {e}")
        conn.cerrar_conexion()
def borrar_libro(id):
    conn = ConexionDB()
    sql = "DELETE FROM Libros WHERE ID = ?"
    
    try:
        conn.cursor.execute(sql, (id,))
        conn.cerrar_conexion()
    except Exception as e:
        print(f"Error al borrar el libro: {e}")
