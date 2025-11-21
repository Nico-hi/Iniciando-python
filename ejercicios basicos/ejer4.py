
combination={
    "uno":{
        "libro":"El Quijote",
        "autor":"Cervantes",
        "precio":20 ,
        "generos":["aventuras","clásico"]
    },
    "dos":{
        "libro":"1984",
        "autor":"Orwell",
        "precio":15 ,
        "generos":["distopía","ficción"]
    },
    "tres":{
        "libro":"cien años de soledad",
        "autor":"Gabriel García Márquez",
        "precio":25 ,
        "generos":["realismo mágico","ficción"]
    }
}

print(f'el segundo elemento es : {combination["dos"]} ')
print("--------------------------------------------------")
#agregar un nuevo libro al diccionario
combination['cuatro']={
    "cuatro":{
        "libro":"Fahrenheit 451",
        "autor":"Ray Bradbury",
        "precio":18 ,
        "generos":["distopía","ciencia ficción"]
    }
}

print(combination)
print("--------------------------------------------------")


set_generos=set()
for number in combination:
    for type in combination[number]:
        if type == "generos":
            set_generos.update(combination[number][type])
            
print(f'los géneros disponibles son: {set_generos}')
print("--------------------------------------------------")

combination['dos']['precio']=17
print(f'el nuevo precio de 1984 es: {combination["dos"]["precio"]}')
print("--------------------------------------------------")


print("--------------------------------------------------")


print("--------------------------------------------------")

