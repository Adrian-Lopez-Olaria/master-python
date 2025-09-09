mi_texto = '"Master"'
# invalido --> mi-texto = "Master"

mi_texto2 = "en \"Python\" "
# invalido --> mi_texto2 = "en "Python" "

texto_unido = mi_texto + " " + mi_texto2
print(texto_unido)

print("-----------------")

# salto de línea con \n
texto_unido = mi_texto + " \n " + mi_texto2
print(texto_unido)
print("-----------------")

# tabulación \t
texto_unido = mi_texto + " \t " + mi_texto2
print(texto_unido)
print("-----------------")

# borrar todo lo de atrar de \r
texto_unido = mi_texto + " \r " + mi_texto2
print(texto_unido)
print("-----------------")