import clases

persona = clases.Persona()
persona.setNombre("Adrián")
persona.setApellidos("López")
persona.setAltura("200cm")
persona.setEdad("500 años")

print(f"La persona es {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())

print("---------------------")

informatico = clases.Informatico()
informatico.setNombre("Carlos")
informatico.setApellidos("Perez")


print(f"El informatico es: {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes())
print(informatico.caminar())
print(informatico.experiencia)

print("---------------------")

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Manolo")
print(tecnico.auditarRedes, tecnico.getNombre(), tecnico.getLenguajes())