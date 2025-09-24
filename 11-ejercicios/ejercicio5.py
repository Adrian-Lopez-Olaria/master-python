"""
Ejercicio 5.
Crear una lista con el contenido de esta tabla:
ACCION         AVENTURA         DEPORTES
GTA             ASSINS           FIFA 21
COD              CRASH            PRO 21
PUGB         Prince of persia    MOTO GP 21
"""

tabla = [
    {
        "categoria": "ACCION",
        "juegos":["GTA", "COD", "PUGB"]
    },
    {
        "categoria": "AVENTURA",
        "juegos":["ASSINS", "CRASH", "Prince of persia"]
    },
    {
        "categoria": "DEPORTES",
        "juegos": ["FIFA 21", "PRO 21", "MOTO GP 21"]
    }
]

for categoria in tabla: # ← 1º bucle: cada "estante/categoría"
    print(f"----------{categoria['categoria']}----------") # ← Nombre del estante
    for juego in categoria['juegos']: # ← 2º bucle: cada "juego" del estante
        print(f"\t{juego}") # ← Mostrar juego individual