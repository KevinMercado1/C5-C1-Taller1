nombre = input("Ingresa tu nombre: ")
fecha_nacimiento = input("Ingresa tu fecha de nacimiento: ")
codigo = input("Ingresa tu codigo de estudiante: ")

datos_estudiante = (nombre, fecha_nacimiento, codigo)
materias = ["Ingles", "Español", "Sociales"]
notas = []

print(f"\nHola, {nombre}, por favor ingresa tus notas:")

for materia in materias:
    nota = float(input(f"Nota para {materia}: "))
    notas.append(nota)

estudiante = {
    "datos": datos_estudiante,
    "notas": notas,
    "materias": materias
}

print("\n--- Registro Completo ---")
print(estudiante) 
