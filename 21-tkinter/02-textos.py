from tkinter import *

ventana = Tk()
ventana.geometry("550x550")


texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
    fg="white",
    bg="#000000",
    padx=40,
    pady=20,
    font=("Consolas", 30)
)
texto.pack()

texto = Label(ventana, text="Soy Adrián")
texto.config(
    bg="orange",
    height=3,
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="spider"
    
)
texto.pack(anchor= SE)

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos} veo que eres de {pais}"


texto = Label(ventana, text=pruebas(pais="España", nombre = "Adrián", apellidos= "López"))
texto.config(
    bg="green",
    height=3,
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="circle"
    
)
texto.pack(anchor= SW)


ventana.mainloop()