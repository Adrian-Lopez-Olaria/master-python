from tkinter import *

ventana = Tk()
ventana.title("Adrián | Master en Python")
ventana.geometry("700x700")

# PRIMER MARCO PADRE (superior)
marco_padre1 = Frame(ventana, width=250, height=250)
marco_padre1.config(
    bg="lightblue",
    
    relief=SOLID
)
marco_padre1.pack(side=TOP, fill=X, expand=YES)

# Marcos hijos dentro del primer marco padre
marco_izquierdo1 = Frame(marco_padre1, width=250, height=250)
marco_izquierdo1.config(
    bg="red",
    bd=5,
    relief=SOLID
)
marco_izquierdo1.pack(side=LEFT, anchor=SW, padx=10, pady=10)

texto = Label(marco_izquierdo1, text="Primer marco")
texto.config(
    bg="red",
    fg="white",
    font=("Arial", 20),
    
)
texto.pack(anchor=CENTER, fill=Y, expand=YES)
marco_izquierdo1.pack_propagate(False)


marco_derecho1 = Frame(marco_padre1, width=250, height=250)
marco_derecho1.config(
    bg="green",
    bd=5,
    relief=SOLID
)
marco_derecho1.pack(side=RIGHT, anchor=SE, padx=10, pady=10)

# SEGUNDO MARCO PADRE (inferior)
marco_padre2 = Frame(ventana, width=250, height=250)
marco_padre2.config(
    bg="lightblue",
    bd=5,
    relief=SOLID
)
marco_padre2.pack(side=TOP, fill=X, expand=YES)

# Marcos hijos dentro del segundo marco padre
marco_izquierdo2 = Frame(marco_padre2, width=250, height=250)
marco_izquierdo2.config(
    bg="blue",
    
    relief=SOLID
)
marco_izquierdo2.pack(side=LEFT, padx=10, pady=10)

marco_derecho2 = Frame(marco_padre2, width=250, height=250)
marco_derecho2.config(
    bg="orange",
    bd=5,
    relief=SOLID
)
marco_derecho2.pack(side=RIGHT, padx=10, pady=10)

ventana.mainloop()