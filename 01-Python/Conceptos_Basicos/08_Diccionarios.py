#DICCIONARIOS


my_dict = {"Nombre" : "Eduardo",
           "Apellido" : "Martín-Sonseca",
           "Edad":25,
           "Lenguajes" : {"Python", "Java", "Kotlin"}}

my_other_dict = {"Nombre" : "Eduardo", "Apellido" : "Martín-Sonseca", "Edad":25}
print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

del my_dict["Nombre"]
print(my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())