import tkinter as tk
from PIL import Image, ImageTk
import studient
import masters
import matter

def menu():
    
    def std():
        studient.estudiantes()
        
    def mst():
        masters.teachers()
        
    def clss():
        matter.materia()
    
    def off():
        ventana_menu.destroy()
        
    def cambiar_color_entrada(event):
        event.widget.config(bg='lightblue')    
    
    def cambiar_color_salida(event):
        event.widget.config(bg='SystemButtonFace')
    
    ventana_menu = tk.Tk()
    ventana_menu.title('Menu')
    ventana_menu.geometry('300x380')
    ventana_menu.config(bg='#589494')
    ventana_menu.resizable(0, 0)

    label = tk.Label(ventana_menu, text="", bg='#589494')
    label.pack()

    img = Image.open('photo.jpg')
    img.thumbnail((200, 200))
    img = ImageTk.PhotoImage(img)

    imgFoto = tk.Label(ventana_menu, image=img)
    imgFoto.pack()

    mensaje = tk.Label(ventana_menu, text="", bg='#589494')
    mensaje.pack()

    Estudiante = tk.Button(ventana_menu, text='ESTUDIANTES',width=20, command=std)
    Estudiante.pack()
    Estudiante.bind('<Enter>', cambiar_color_entrada)
    Estudiante.bind('<Leave>', cambiar_color_salida)

    mensaje = tk.Label(ventana_menu, text="", bg='#589494')
    mensaje.pack()

    Docente = tk.Button(ventana_menu, text='DOCENTES',width=20, command= mst)
    Docente.pack()
    Docente.bind('<Enter>', cambiar_color_entrada)
    Docente.bind('<Leave>', cambiar_color_salida)

    mensaje = tk.Label(ventana_menu, text="", bg='#589494')
    mensaje.pack()

    Materias = tk.Button(ventana_menu, text='MATERIAS',width=20, command= clss)
    Materias.pack()
    Materias.bind('<Enter>', cambiar_color_entrada)
    Materias.bind('<Leave>', cambiar_color_salida)

    mensaje = tk.Label(ventana_menu, text="", bg='#589494')
    mensaje.pack()

    Cerrar = tk.Button(ventana_menu, text='CERRAR SESION',width=20, command= off)
    Cerrar.pack()
    Cerrar.bind('<Enter>', cambiar_color_entrada)
    Cerrar.bind('<Leave>', cambiar_color_salida)

    mensaje = tk.Label(ventana_menu, text="", bg='#589494')
    mensaje.pack()

    ventana_menu.mainloop()
