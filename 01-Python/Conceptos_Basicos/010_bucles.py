#Bucles

#While

print("BUCLE WHILE")
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition+=2

else:
    print("Mi condicion es mayor o igual que 10")

print("La ejecucion continua")

while my_condition < 20 :
    my_condition+=1

    if my_condition == 15:
        print("Mi condicion es 15")
        break

    print(my_condition)


print("BUCLE FOR")
    #For itera un listado de elementos

print("LISTA")
my_list = [25,32,15,25,78,58,25]
for element in my_list :
    print(element)

print("TUPLA")
my_tuple = (35,1.85,"Eduardo", "Martín-Sonseca", "Eduardo")
for element in my_tuple :
    print(element)

print("SET")
my_set = {"Eduardo",25, "maraloedev"}
for element in my_set :
    print(element)

print("DICCIONARIO")
my_dict = {"Nombre" : "Eduardo", "Apellido" : "Martín-Sonseca", "Edad":25}
for element in my_dict :
    print(element)

    if element == "Edad":
        break
else:
    print("El bucle for para mi diccionario a finalizado")

print("La ejecucion continua")


for element in my_dict :
    print(element)

    if element == "Edad":
        continue
else:
    print("El bucle for para mi diccionario a finalizado")
