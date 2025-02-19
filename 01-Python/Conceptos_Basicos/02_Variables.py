#Variables

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable=5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable=True
print(my_bool_variable)

#COncatenacion de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de ", my_bool_variable)

#Algunas funciones del sistema
print(len(my_string_variable))

#Variables en una sola linea
name, surname, alias, ages = "Eduardo", "Martin-Sonseca", "maraloedev", 25

print("Me llamo: ",name, surname, " mi alias es", alias,". Mi edad es ", ages)

#Pedir datos al usuario se una input
#name = input("Como te llamas")
#age = input("Cuantos años tienes")

# Cambiamos su tipo
name = 35
ages = "Eduardo"
print(name)
print(ages)

#Forzamos el tipo
address: str = "Mi direccion"
print(type(address))