# Tkinter
# Modulo para crear interfaces graficas de usuario

from tkinter import *
import os.path

class Programa:

    def __init__(self):
        self.title = "Master en Python"
        self.icon = './imagenes/logo-python.ico'
        self.icon_alt = './21-tkinter/imagenes/logo-python.ico'
        self.size = "750x450"
        self.resizable = False

    def cargar(self):
        # Crear la ventana raiz
        self.ventana = Tk()

        # Título de la ventana
        self.ventana.title(self.title)

        # Comprobar si existe un archivo
        ruta_icono = os.path.abspath(self.icon)
        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)

        # Mostrar texto en el programa (la ruta absoluta de la imagen)      
        texto = Label(self.ventana, text = ruta_icono)
        texto.pack()

        # Icono de la ventana
        self.ventana.iconbitmap(ruta_icono)

        # Tamaño de la ventana
        self.ventana.geometry(self.size)

        # Bloquear el tamaño de la ventana
        if self.resizable:
            self.ventana.resizable(1, 1)
        else:
            self.ventana.resizable(0, 0)

    def addTexto(self, dato):
        # Mostrar texto en el programa
        texto = Label(self.ventana, text= dato)
        texto.pack()

    def mostrar(self):
        # Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()

# Instanciar mi programa
programa = Programa()
programa.cargar()
programa.addTexto("Hola")
programa.addTexto("Soy un texto")
programa.addTexto("Saludos")
programa.mostrar()