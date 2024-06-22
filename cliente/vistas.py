import tkinter as tk
from tkinter import ttk, messagebox
from modelo.consultas_dao import Libros, listar_generos, listar_editoriales, listar_libros, guardar_libro, editar_libro, borrar_libro

def barrita_menu(root):
    barra = tk.Menu(root, bg="lightblue")
    root.config(menu=barra, width=300, height=300)
    
    menu_inicio = tk.Menu(barra, tearoff=0, bg="lightblue")  
    menu_consultas = tk.Menu(barra, tearoff=0, bg="lightblue")
    menu_acerca_de = tk.Menu(barra, tearoff=0, bg="pink")
    menu_ayuda = tk.Menu(barra, tearoff=0, bg="red")
    
    menu_inicio.add_command(label='Conectar DB', command=conectar_db)
    menu_inicio.add_command(label='Desconectar DB', command=desconectar_db)
    menu_inicio.add_command(label='Salir', command=lambda: salir_app(root))
    
    barra.add_cascade(label='Inicio', menu=menu_inicio)
    barra.add_cascade(label='Consultas', command=consultas)
    barra.add_cascade(label='Acerca de..', command=acerca_de)
    barra.add_cascade(label='Ayuda', command=ayuda)



class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320, bg="lightblue")
        self.root = root
        self.pack()
        self.id_libro = None

        self.label_form()
        self.input_form()
        self.botones_principales()
        self.mostrar_tabla()

    def label_form(self):
        self.label_titulo = tk.Label(self, text="Título: ")
        self.label_titulo.config(font=('Arial', 12, 'bold'))
        self.label_titulo.grid(row=0, column=0, padx=10, pady=10)

        self.label_autor = tk.Label(self, text="Autor: ")
        self.label_autor.config(font=('Arial', 12, 'bold'))
        self.label_autor.grid(row=1, column=0, padx=10, pady=10)

        self.label_genero = tk.Label(self, text="Género: ")
        self.label_genero.config(font=('Arial', 12, 'bold'))
        self.label_genero.grid(row=2, column=0, padx=10, pady=10)

        self.label_editorial = tk.Label(self, text="Editorial: ")
        self.label_editorial.config(font=('Arial', 12, 'bold'))
        self.label_editorial.grid(row=3, column=0, padx=10, pady=10)

        self.label_anio = tk.Label(self, text="Año: ")
        self.label_anio.config(font=('Arial', 12, 'bold'))
        self.label_anio.grid(row=4, column=0, padx=10, pady=10)

        self.label_isbn = tk.Label(self, text="ISBN: ")
        self.label_isbn.config(font=('Arial', 12, 'bold'))
        self.label_isbn.grid(row=5, column=0, padx=10, pady=10)

    def input_form(self):
        self.titulo = tk.StringVar()
        self.entry_titulo = tk.Entry(self, textvariable=self.titulo)
        self.entry_titulo.config(width=50, state='disabled', font=('Arial', 12))
        self.entry_titulo.grid(row=0, column=1, padx=10, pady=10, columnspan='2')

        self.autor = tk.StringVar()
        self.entry_autor = tk.Entry(self, textvariable=self.autor)
        self.entry_autor.config(width=50, state='disabled', font=('Arial', 12))
        self.entry_autor.grid(row=1, column=1, padx=10, pady=10, columnspan='2')

         # Lista de géneros por defecto
        generos = ['Seleccione uno', 'Ficción', 'No ficción', 'Ciencia ficción', 'Fantasía', 
                  'Misterio', 'Romance', 'Thriller', 'Biografía', 'Historia', 'Poesía']
        self.entry_genero = ttk.Combobox(self, state="readonly", values=generos)
        self.entry_genero.current(0)
        self.entry_genero.config(width=25, state='disabled', font=('Arial', 12))
        self.entry_genero.grid(row=2, column=1, padx=10, pady=10, columnspan='2')

         # Lista de editoriales por defecto
        editoriales = ['Seleccione uno', 'Penguin Random House', 'HarperCollins', 'Simon & Schuster', 'Macmillan Publishers', 
                   'Hachette Livre', 'Scholastic Corporation', 'Pearson Education', 'Springer Nature', 'Oxford University Press', 'Cambridge University Press']
         
        self.entry_editorial = ttk.Combobox(self, state="readonly", values=editoriales)
        self.entry_editorial.current(0)
        self.entry_editorial.config(width=25, state='disabled', font=('Arial', 12))
        self.entry_editorial.grid(row=3, column=1, padx=10, pady=10, columnspan='2')

        self.anio = tk.StringVar()
        self.entry_anio = tk.Entry(self, textvariable=self.anio)
        self.entry_anio.config(width=50, state='disabled', font=('Arial', 12))
        self.entry_anio.grid(row=4, column=1, padx=10, pady=10, columnspan='2')

        self.isbn = tk.StringVar()
        self.entry_isbn = tk.Entry(self, textvariable=self.isbn)
        self.entry_isbn.config(width=50, state='disabled', font=('Arial', 12))
        self.entry_isbn.grid(row=5, column=1, padx=10, pady=10, columnspan='2')

    def botones_principales(self):
        self.btn_nuevo = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.btn_nuevo.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1C500B', cursor='hand2', activebackground='#3FD83F', activeforeground='#000000')
        self.btn_nuevo.grid(row=6, column=0, padx=10, pady=10)

        self.btn_guardar = tk.Button(self, text='Guardar', command=self.guardar_campos)
        self.btn_guardar.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#0D2A83', cursor='hand2', activebackground='#7594F5', activeforeground='#000000', state='disabled')
        self.btn_guardar.grid(row=6, column=1, padx=10, pady=10)

        self.btn_cancelar = tk.Button(self, text='Cancelar', command=self.bloquear_campos)
        self.btn_cancelar.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#A90A0A', cursor='hand2', activebackground='#F35B5B', activeforeground='#000000', state='disabled')
        self.btn_cancelar.grid(row=6, column=2, padx=10, pady=10)

        self.btn_editar = tk.Button(self, text='Editar', command=self.editar_campos)
        self.btn_editar.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#A87E0A', cursor='hand2', activebackground='#F3D15B', activeforeground='#000000', state='disabled')
        self.btn_editar.grid(row=8, column=0, padx=10, pady=10, columnspan='2')

        self.btn_eliminar = tk.Button(self, text='Eliminar', command=self.eliminar_libro)
        self.btn_eliminar.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#A90A0A', cursor='hand2', activebackground='#F35B5B', activeforeground='#111111', state='disabled')
        self.btn_eliminar.grid(row=8, column=1, padx=10, pady=10, columnspan='2')

    def habilitar_campos(self):
        self.entry_titulo.config(state='normal')
        self.entry_autor.config(state='normal')
        self.entry_genero.config(state='normal')
        self.entry_editorial.config(state='normal')
        self.entry_anio.config(state='normal')
        self.entry_isbn.config(state='normal')
        self.btn_guardar.config(state='normal')
        self.btn_cancelar.config(state='normal')
        self.btn_nuevo.config(state='disabled')
        self.btn_editar.config(state='disabled')
        self.btn_eliminar.config(state='disabled')

    def bloquear_campos(self):
        self.entry_titulo.config(state='disabled')
        self.entry_autor.config(state='disabled')
        self.entry_genero.config(state='disabled')
        self.entry_editorial.config(state='disabled')
        self.entry_anio.config(state='disabled')
        self.entry_isbn.config(state='disabled')
        
        # Limpiar los campos 
        self.titulo.set('')
        self.autor.set('')
        self.entry_genero.current(0)
        self.entry_editorial.current(0)
        self.anio.set('')
        self.isbn.set('')
        
        self.id_libro = None

        self.btn_nuevo.config(state='normal')
        self.btn_editar.config(state='disabled')
        self.btn_eliminar.config(state='disabled')
        self.btn_guardar.config(state='disabled')
        self.btn_cancelar.config(state='disabled')


    def guardar_campos(self):
        libro = Libros(
            self.titulo.get(),
            self.autor.get(),
            self.entry_genero.get(),
            self.entry_editorial.get(),
            self.anio.get(),
            self.isbn.get()
        )

        if self.id_libro is None:
            guardar_libro(libro)
        else:
            editar_libro(libro, self.id_libro)

        self.mostrar_tabla()
        self.bloquear_campos()

    def editar_campos(self):
        try:
            self.id_libro = self.tabla.item(self.tabla.selection())['text']
            self.titulo.set(self.tabla.item(self.tabla.selection())['values'][0])
            self.autor.set(self.tabla.item(self.tabla.selection())['values'][1])
            self.entry_genero.set(self.tabla.item(self.tabla.selection())['values'][2])
            self.entry_editorial.set(self.tabla.item(self.tabla.selection())['values'][3])
            self.anio.set(self.tabla.item(self.tabla.selection())['values'][4])
            self.isbn.set(self.tabla.item(self.tabla.selection())['values'][5])
            self.habilitar_campos()
            self.btn_editar.config(state='normal')
            self.btn_eliminar.config(state='normal')
        except IndexError:
            messagebox.showerror('Error', 'Selecciona un libro de la tabla')

    def eliminar_libro(self):
        try:
            self.id_libro = self.tabla.item(self.tabla.selection())['text']
            libro_eliminado = self.tabla.item(self.tabla.selection())['values'][0]
            if messagebox.askquestion('Eliminar', f'¿Está seguro de eliminar el libro {libro_eliminado}?') == messagebox.YES:
                borrar_libro(self.id_libro)
                self.mostrar_tabla()
                self.id_libro = None
                self.btn_editar.config(state='disabled')
                self.btn_eliminar.config(state='disabled')
        except IndexError:
            messagebox.showerror('Error', 'Selecciona un libro de la tabla')

    def mostrar_tabla(self):
        self.lista_libros = listar_libros()
        self.lista_libros.reverse()
        self.tabla = ttk.Treeview(self, columns=('Titulo', 'Autor', 'Genero', 'Editorial', 'Año', 'ISBN'))

        self.tabla.grid(row=7, column=0, columnspan=4, sticky='nse', padx=10, pady=10)
        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=7, column=4, sticky='nse', padx=10, pady=10)
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Título')
        self.tabla.heading('#2', text='Autor')
        self.tabla.heading('#3', text='Género')
        self.tabla.heading('#4', text='Editorial')
        self.tabla.heading('#5', text='Año')
        self.tabla.heading('#6', text='ISBN')

        self.tabla.column('#0', minwidth=30, width=50)
        self.tabla.column('#1', minwidth=50, width=100)
        self.tabla.column('#2', minwidth=50, width=100)
        self.tabla.column('#3', minwidth=50, width=100)
        self.tabla.column('#4', minwidth=50, width=100)
        self.tabla.column('#5', minwidth=50, width=100)
        self.tabla.column('#6', minwidth=50, width=100)

        for libro in self.lista_libros:
            
            self.tabla.insert('', 0, text=libro[0], values=(libro[1], libro[2], libro[3], libro[4], libro[5], libro[6]))

        self.tabla.bind('<<TreeviewSelect>>', self.habilitar_editar_eliminar)

    def habilitar_editar_eliminar(self, event):
        self.btn_editar.config(state='normal')
        self.btn_eliminar.config(state='normal')

  #funciones para manejar la barrita_menu      
def conectar_db():
    
    messagebox.showinfo("Conectar DB", "Conexión a la base de datos establecida existosamente.")

def desconectar_db():
    
    messagebox.showinfo("Desconectar DB", "Conexión a la base de datos cerrada existosamente.")

def salir_app(root):
    respuesta = messagebox.askyesno("Salir", "¿Está seguro de que desea salir?")
    if respuesta:
        respuesta = messagebox.askyesno("¿En serio? ", "¿En serio? ¿Estás seguro de querer salir?")
        if respuesta:
            respuesta = messagebox.askyesno("¿Posta?", "¿Posta queres salir? -;-")
            if respuesta:
                respuesta = messagebox.askyesno("Hasta Pronto", "Gracias por utilizar mi aplicación. ¿Está seguro de que desea salir?")
                if respuesta:
                    root.destroy()

def consultas():
    
    messagebox.showinfo("Consultas", "Realizando consulta...")

def acerca_de():
   
    messagebox.showinfo("Acerca de..", "Esta aplicación fue desarrollada para gestionar una biblioteca.")

def ayuda():
    
    messagebox.showinfo("Ayuda", "Para obtener ayuda, contacte con soporte.")

