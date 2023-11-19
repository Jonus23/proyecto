import mysql.connector
import tkinter as tk
from tkinter import ttk

def materia():
    root = tk.Tk()
    root.title("Lista de materias")

    conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="jasr2004.", 
                database="proyecto-final"
            )

    cursor = conexion.cursor()
    consulta = 'SELECT `id_clase`, `nombre_clase`, `carrera_relacionada` FROM `clases`'
    cursor.execute(consulta)
    clase = cursor.fetchall()
    
    cursor.close()
    conexion.close()
    
    materias = ttk.Treeview(root, columns=('id_clase', 'nombre_clase', 'carrera_relacionada'))
    materias.heading('id_clase', text= 'ID')
    materias.heading('nombre_clase', text= 'Clase')
    materias.heading('carrera_relacionada', text= 'Carrera')

    
    for clas in clase:
        materias.insert('','end', values= clas)
        materias.pack()
        
    root.mainloop()
    

materia()