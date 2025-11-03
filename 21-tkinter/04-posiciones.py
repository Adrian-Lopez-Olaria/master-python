from tkinter import *

ventana = Tk()
# ventana.geometry("550x550")

texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
    fg="white",
    bg="#000000",
    padx=40,
    pady=20,
    font=("Consolas", 30)
)
texto.pack(side=TOP)  # CORRECCIÓN: Cambiado size por side

texto = Label(ventana, text="Soy Adrián")
texto.config(
    bg="orange",
    height=3,
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="spider"
)
texto.pack(
    side=TOP, 
    fill=X, # Para rellenar toda la posición
    expand=YES)

texto = Label(ventana, text="Basico 1")
texto.config(
    bg="green",
    height=3,
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="circle"
)
texto.pack(side= LEFT, fill=X, expand=YES)

texto = Label(ventana, text="Basico 2")
texto.config(
    bg="red",
    height=3,
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="circle"
)
texto.pack(side= LEFT, fill=X, expand=YES)

texto = Label(ventana, text="Basico 3")
texto.config(
    bg="pink",
    height=3,
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="circle"
)
texto.pack(side= LEFT, fill=X, expand=YES)

ventana.mainloop()