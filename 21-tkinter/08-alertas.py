from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.config(bd=70)

def sacarAlertaInfo():
    MessageBox.showinfo("Alerta", "Hola soy Adrián")

Button(ventana, text="Mostrar alerta info!!!", command=sacarAlertaInfo).pack(padx=20,pady=20)

def sacarAlertaWarning():
    MessageBox.showwarning("Warnig", "Hola soy una alerta de warning")

Button(ventana, text="Mostrar alerta warning!!!", command=sacarAlertaWarning).pack(padx=20,pady=20)

def sacarAlertaError():
    MessageBox.showerror("Error", "Hola soy una alerta de error")

Button(ventana, text="Mostrar alerta error!!!", command=sacarAlertaError).pack(padx=20,pady=20)

def salir(nombre):
    resultado = MessageBox.askquestion("Salir", "¿Continuar ejecutando la aplicación?")
    
    if resultado != "yes":
        MessageBox.showinfo("Chao!!", f"Adiós {nombre} hasta pronto")
        ventana.destroy()

Button(ventana, text="Salir", command=lambda: salir("Adrián")).pack(padx=20,pady=20)




ventana.mainloop()