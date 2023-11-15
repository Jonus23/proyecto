import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Inicio de sesión')
root.geometry('400x330')
root.config(bg='#589494')
root.resizable(0,0)

mensaje_label = tk.Label(root, text="",bg='#589494')
mensaje_label.pack()

img = Image.open('photo.jpg')
img.thumbnail((200, 200))
img = ImageTk.PhotoImage(img)

imgFoto = tk.Label(image=img)
imgFoto.pack()

mensaje_label = tk.Label(root, text="",bg='#589494')
mensaje_label.pack()

usuario = Label(root, text='Usuario', bg='#589494')
usuario.pack()

usuario = tk.Entry(root)
usuario.pack()

password = Label(root, text='Contraseña', bg='#589494')
password.pack()

contraseña = tk.Entry(root, show="*")  
contraseña.pack()

mensaje_label = tk.Label(root, text="",bg='#589494')
mensaje_label.pack()

botton = tk.Button(root, text='Iniciar Sesión')
botton.pack()





root.mainloop()
