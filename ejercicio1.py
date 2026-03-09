
nombre =input("Ingresa tu nombre: ")
fecha_nacimiento = input("Ingresa tu fecha de nacimiento: ")
codigo =input("Ingresa tu codigo de estudiante: ")

datos_estudiante = (nombre, fecha_nacimiento, codigo)

notas = [3.0,4.5,5.0]

estudiante = {
"datos": datos_estudiante,
"notas": notas
}

materias = ["Ingles", "Español", "Sociales"]

print(estudiante)
print(materias)