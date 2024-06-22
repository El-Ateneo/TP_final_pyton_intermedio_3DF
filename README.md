# TP_final_pyton_intermedio_3DF
trabajo final curso intermedio de python dictado por la municipalidad de 3 de Febrero

Gestión de Libros
Este proyecto es una aplicación de gestión de libros desarrollada en Python utilizando Tkinter para la interfaz gráfica y SQLite para la base de datos. La aplicación permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una base de datos de libros, géneros y editoriales.

Requisitos
Python 3.x
Tkinter
SQLite3

Instalación
Clona el repositorio en tu máquina local:

git clone https://github.com/El-Ateneo/TP_final_pyton_intermedio_3DF.git

Navega al directorio del proyecto:

cd gestion-de-libros

Uso
Ejecuta el archivo principal para iniciar la aplicación:

python principal.py

La aplicación abrirá una ventana donde podrás gestionar tus libros, géneros y editoriales.


Funcionalidades
Agregar Libro: Permite agregar un nuevo libro a la base de datos.
Editar Libro: Permite seleccionar un libro de la lista, rellenar automáticamente los campos y actualizar los datos del libro.
Eliminar Libro: Permite eliminar un libro de la base de datos tras confirmar la acción.
Listar Libros: Muestra una lista de todos los libros en la base de datos.
Listar Géneros y Editoriales: Carga al menos 10 géneros y 10 editoriales para seleccionar al agregar o editar un libro.

Archivos Principales
principal.py
Este archivo contiene el punto de entrada de la aplicación. Configura la ventana principal y el menú.

cliente/vistas.py
Este archivo contiene la definición de la interfaz gráfica utilizando Tkinter. Incluye la creación de widgets, la carga de datos y las acciones de los botones.

cliente/consultas_dao.py
Este archivo contiene las funciones para interactuar con la base de datos SQLite. Incluye la creación de tablas, la inserción, actualización, eliminación y listado de registros.

Contribuciones
Las contribuciones son bienvenidas. Por favor, crea un fork del repositorio y envía un pull request con tus mejoras.

Licencia
Este proyecto está licenciado bajo la Licencia MIT.
