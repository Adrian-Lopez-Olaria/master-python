from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("700x600")

Label(ventana, text="Hola, soy Adrián!!").pack(anchor=W)

imagen = Image.open('./21-tkinter/imagenes/galaxia.jpg')
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack(anchor=E)


ventana.mainloop()