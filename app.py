import tkinter as tk
from PIL import Image, ImageTk

def menu():
    ventana_menu = tk.Tk()
    ventana_menu.title('Menu')
    ventana_menu.geometry('300x350')
    ventana_menu.config(bg='#589494')
    ventana_menu.resizable(0, 0)

    label = tk.Label(ventana_menu, text="", bg='#589494')
    label.pack()

    img = Image.open('opciones\photo.jpg')
    img.thumbnail((200, 200))
    img = ImageTk.PhotoImage(img)

    imgFoto = tk.Label(ventana_menu, image=img)
    imgFoto.pack()

    mensaje = tk.Label(ventana_menu, text="", bg='#589494')
    mensaje.pack()

    estudiante = tk.Button(ventana_menu, text='ESTUDIANTES')
    estudiante.pack()

    mensaje = tk.Label(ventana_menu, text="", bg='#589494')
    mensaje.pack()

    Docente = tk.Button(ventana_menu, text='DOCENTES')
    Docente.pack()

    mensaje = tk.Label(ventana_menu, text="", bg='#589494')
    mensaje.pack()

    Materias = tk.Button(ventana_menu, text='MATERIAS')
    Materias.pack()

    mensaje = tk.Label(ventana_menu, text="", bg='#589494')
    mensaje.pack()

    ventana_menu.mainloop()


