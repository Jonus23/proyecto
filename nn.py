import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
import app
    
def Inicio():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jasr2004.",
        database="proyecto-final"
    )

    cursor = conexion.cursor()
    cursor.execute('SELECT usuario, contraseña FROM `ingreso` WHERE 1')
    resultado = cursor.fetchone()

    if resultado is not None:
        usuario_bd, contraseña_bd = resultado
        usuario_ingresado = usuarioEntry.get()
        contraseña_ingresada = contraseñaEntry.get()

        if usuario_ingresado == usuario_bd and contraseña_ingresada == contraseña_bd:
            mensaje.config(text='Inicio de sesión válida')
            root.destroy()
            app.menu()

        else:
            mensaje.config(text='Inicio de sesión inválida')
    else:
        mensaje.config(text='Usuario no encontrado en la base de datos')

    cursor.close()
    conexion.close()

def cambiar_color_entrada(event):
        event.widget.config(bg='red')    
    
def cambiar_color_salida(event):
    event.widget.config(bg='SystemButtonFace')
    
def on():
    root.destroy()
        
root = tk.Tk()
root.title('Inicio de sesión')
root.geometry('370x330')
root.config(bg='#589494')
root.resizable(0,0)
root.iconbitmap('kisspng-computer-icons-technology-symbol-icon-design-5b0037144a7b63.ico')

label = tk.Label(root, text="",bg='#589494')
label.pack()

img = Image.open('photo.jpg')
img.thumbnail((200, 200))
img = ImageTk.PhotoImage(img)

imgFoto = tk.Label(image=img)
imgFoto.pack()

mensaje = tk.Label(root, text="",bg='#589494')
mensaje.pack()

usuario = Label(root, text='Usuario', bg='#589494')
usuario.pack()

usuarioEntry = tk.Entry(root)
usuarioEntry.pack()

contraseña_ = Label(root, text='Contraseña', bg='#589494')
contraseña_.pack()

contraseñaEntry = tk.Entry(root, show="*")  
contraseñaEntry.pack()

label = tk.Label(root, text="",bg='#589494')
label.pack()

boton = tk.Button(root, text='Iniciar Sesión', command= Inicio)
boton.pack()
boton.bind('<Enter>', cambiar_color_entrada)
boton.bind('<Leave>', cambiar_color_salida)

root.mainloop()

    
