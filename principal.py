import tkinter as tk
from cliente.vistas import Frame, barrita_menu
#from modelo.consultas_dao import crear_tablas
#para crear la base de datos por primera vez habilite la opciones que estan comentadas(#from modelo.consultas_dao import crear_tablas y #crear_tablas())
def main():
    #crear_tablas()
    root = tk.Tk()
    root.title('Gestor de Libros')
    root.iconbitmap('img/libro1.ico')
    root.resizable(0,0)

    barrita_menu(root)
    app = Frame(root=root)
   
    app.mainloop()

if __name__ == "__main__":
    main()