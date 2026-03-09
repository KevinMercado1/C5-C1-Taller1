mascota = {
"nombre": "chocolate",
"color": ["negro", "blanco"],
"especie": "perro",
"raza": "Dogo Argentino",
"estado_de_animalito": "saludable",
"peso": "35.0",
"vacunado": True,
"dueño": {
"nombre": "Kevin",
"chip": 23433,
"apellido": "Mercado",
"telefono": "235-6453"
}
},


# print(mascota.get("nombre"))
# print(mascota.get("raza"))
# print(mascota.get("dueño").get("nombre"))

for mascota in mascota:
    print(mascota["nombre"])
    print(mascota["dueño"]["nombre"])
    print(mascota["dueño"]["apellido"])
    print(mascota["dueño"]["telefono"])
    print("-----------------------")