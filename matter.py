import mysql.connector
import tkinter as tk
from tkinter import ttk

def materia():
    
    def cambiar_color_entrada(event):
        event.widget.config(bg='red')    
    
    def cambiar_color_salida(event):
        event.widget.config(bg='SystemButtonFace')
    
    def off():
        matter.destroy()
   
    matter = tk.Toplevel()
    matter.title("Lista de materias")
    matter.iconbitmap('kisspng-computer-icons-technology-symbol-icon-design-5b0037144a7b63.ico')

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
    
    materias = ttk.Treeview(matter, columns=('id_clase', 'nombre_clase', 'carrera_relacionada'))
    materias.heading('id_clase', text= 'ID')
    materias.heading('nombre_clase', text= 'Clase')
    materias.heading('carrera_relacionada', text= 'Carrera')

    
    for clas in clase:
        materias.insert('','end', values= clas)
        materias.pack()
    
    Cerrar = tk.Button(matter, text='CERRAR',width=20, command= off)
    Cerrar.pack()
    Cerrar.bind('<Enter>', cambiar_color_entrada)
    Cerrar.bind('<Leave>', cambiar_color_salida)
    
    matter.mainloop()
