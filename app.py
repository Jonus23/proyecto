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

    Estudiante = tk.Button(ventana_menu, text='ESTUDIANTES', command=std)
    Estudiante.pack()

    mensaje = tk.Label(ventana_menu, text="", bg='#589494')
    mensaje.pack()

    Docente = tk.Button(ventana_menu, text='DOCENTES', command= mst)
    Docente.pack()

    mensaje = tk.Label(ventana_menu, text="", bg='#589494')
    mensaje.pack()

    Materias = tk.Button(ventana_menu, text='MATERIAS', command= clss)
    Materias.pack()

    mensaje = tk.Label(ventana_menu, text="", bg='#589494')
    mensaje.pack()

    Cerrar = tk.Button(ventana_menu, text='CERRAR SESION', command= off)
    Cerrar.pack()

    mensaje = tk.Label(ventana_menu, text="", bg='#589494')
    mensaje.pack()

    ventana_menu.mainloop()


