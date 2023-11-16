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
    usuario = cursor.execute('SELECT usuario')
    contraseña = cursor.execute('SELECT contraseña')

    Usu = usuarioEntry.get()
    password = contraseñaEntry.get()
    
    
    if Usu == usuario and password == contraseña:
        mensaje.config(text='Inicio de sesión valida')
    else:
        mensaje.config(text='Inicio de sesión invalida')

    cursor.close()
    conexion.close()

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
