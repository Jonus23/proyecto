import mysql.connector
import tkinter as tk
from tkinter import ttk


def estudiantes():
    root = tk.Tk()
    root.title("Lista de estudiantes")

    conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="jasr2004.", 
                database="proyecto-final"
            )

    cursor = conexion.cursor()
    consulta = 'SELECT `codigo`, `nombre`, `apellido`, `celular`, `carrera` FROM `estudiantes`'
    cursor.execute(consulta)
    student = cursor.fetchall()
    
    cursor.close()
    conexion.close()
    
    estudiantes = ttk.Treeview(root, columns=('Código', 'Nombre', 'Apellido', 'Celular', 'Carrera'))
    estudiantes.heading('Código', text= 'Código')
    estudiantes.heading('Nombre', text= 'Nombre')
    estudiantes.heading('Apellido', text= 'Apellido')
    estudiantes.heading('Celular', text= 'Celular')
    estudiantes.heading('Carrera', text= 'Carrera')
    
    for std in student:
        estudiantes.insert('','end', values= std)
        estudiantes.pack()
        
    root.mainloop()
    
