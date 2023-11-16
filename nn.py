import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector

def Inicio ():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jasr2004.", 
        database="proyecto-final"
    )
        
    cursor = conexion.cursor()
    cursor.execute('SELECT usuario, contraseña FROM `ingreso` WHERE 1')  # Reemplaza 'nombre_de_la_tabla' con el nombre real de tu tabla
    resultado = cursor.fetchone()

    if resultado is not None:
        usuario_bd, contraseña_bd = resultado
        usuario_ingresado = usuarioEntry.get()
        contraseña_ingresada = contraseñaEntry.get()

        if usuario_ingresado == usuario_bd and contraseña_ingresada == contraseña_bd:
            mensaje.config(text='Inicio de sesión válida')
        else:
            mensaje.config(text='Inicio de sesión inválida')
    else:
        mensaje.config(text='Usuario no encontrado en la base de datos')

    cursor.close()
    conexion.close()
    
    root.after(5000, root.destroy)
    
root = tk.Tk()
root.title('Inicio de sesión')
root.geometry('400x330')
root.config(bg='#589494')
root.resizable(0,0)

label = tk.Label(root, text="",bg='#589494')
label.pack()

img = Image.open('proyecto\photo.jpg')
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




root.mainloop()
