nombre = input("Ingresa tu nombre: ")
fecha_nacimiento = input("Ingresa tu fecha de nacimiento: ")
codigo = input("Ingresa tu codigo de estudiante: ")

datos_estudiante = (nombre, fecha_nacimiento, codigo)
materias = ["Ingles", "Español", "Sociales"]

calificaciones = {}

print(f"\nHola, {nombre}, por favor ingresa tus notas:")

for materia in materias:
    try:
        nota = float(input(f"Nota para {materia}: "))
        calificaciones[materia] = nota
    except ValueError:
        print(f"Error en {materia}: No se pueden colocar letras u caracteres especiales.")
        calificaciones[materia] = 0.0 

estudiante = {
    "perfil": datos_estudiante,
    "notas_por_materia": calificaciones
}

print("\n--- Registro Completo ---")
print(estudiante) 