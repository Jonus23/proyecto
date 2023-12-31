import mysql.connector
import tkinter as tk
from tkinter import ttk


def estudiantes():
    
    def cambiar_color_entrada(event):
        event.widget.config(bg='red')    
    
    def cambiar_color_salida(event):
        event.widget.config(bg='SystemButtonFace')
    
    def off():
        root.destroy()
    
    root = tk.Toplevel()
    root.title("Lista de estudiantes")
    root.iconbitmap('kisspng-computer-icons-technology-symbol-icon-design-5b0037144a7b63.ico')

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
    
    Cerrar = tk.Button(root, text='CERRAR',width=20, command= off)
    Cerrar.pack()
    Cerrar.bind('<Enter>', cambiar_color_entrada)
    Cerrar.bind('<Leave>', cambiar_color_salida)
    
    root.mainloop()
    
