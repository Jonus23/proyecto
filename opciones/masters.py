import mysql.connector
import tkinter as tk
from tkinter import ttk


def teachers():
    root = tk.Tk()
    root.title("Lista de Docentes")

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
        
    root.mainloop()
    