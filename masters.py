import mysql.connector
import tkinter as tk
from tkinter import ttk


def teachers():
   
    def cambiar_color_entrada(event):
        event.widget.config(bg='red')    
    
    def cambiar_color_salida(event):
        event.widget.config(bg='SystemButtonFace')
    
    def off():
        root.destroy()
   
    root = tk.Toplevel()
    root.title("Lista de Docentes")
    root.iconbitmap('kisspng-computer-icons-technology-symbol-icon-design-5b0037144a7b63.ico')

    conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="jasr2004.", 
                database="proyecto-final"
            )

    cursor = conexion.cursor()
    consulta = 'SELECT `id_docente`, `nombre_docente`, `apellido_docente`, `clase_relacionada` FROM `docentes`'
    cursor.execute(consulta)
    master = cursor.fetchall()
    
    cursor.close()
    conexion.close()
    
    Docentes = ttk.Treeview(root, columns=('id_docente', 'nombre_docente', 'apellido_docente', 'clase_relacionada'))
    Docentes.heading('id_docente', text= 'Id')
    Docentes.heading('nombre_docente', text= 'Nombre')
    Docentes.heading('apellido_docente', text= 'Apellido')
    Docentes.heading('clase_relacionada', text= 'Materia')
    
    for Tcr in master:
        Docentes.insert('','end', values= Tcr)
        Docentes.pack()
        
    Cerrar = tk.Button(root, text='CERRAR',width=20, command= off)
    Cerrar.pack()
    Cerrar.bind('<Enter>', cambiar_color_entrada)
    Cerrar.bind('<Leave>', cambiar_color_salida)
    
    root.mainloop()
    