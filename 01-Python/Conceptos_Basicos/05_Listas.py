#LISTAS

my_list = [25,32,15,25,78,58,25]

print(len(my_list))

my_other_list = [25,1.85, "Eduardo", "Martin-Sonseca", 25, 25]
print(f"LISTAS \n {my_list} \n {my_other_list}")


print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1]) # El -1 imprime el ultimo elemento
print(my_other_list[-3])
print(my_other_list.count(25)) # El count sirve para saber cuantas veces se repite un valor

print(my_other_list + my_list)
print(my_other_list[0] * my_list[0])

print("AÑADO DATOS A LA LISTA")
my_other_list.append("maraloedev")
print(my_other_list)

print("INSERTO DATOS A LA LISTA EN LA POSICION QUE QUIERO")
my_other_list.insert(0,"Hola") # insert sirve para añadir el valor que tu quieras en una posicion
print(my_other_list)

print("ELIMINO DATOS DE LA LISTA")
my_other_list.remove("Hola")
print(my_other_list)

print("ELIMINO DATOS DE LA LISTA QUE SE QUE ESTAN EN ELLA")
my_list.remove(25)
print(my_list)

print("Elimina el ultimo elemento de la lista, o el que tu le pongas, en mi caso, elimino el elemento 1")
my_list.pop()
print(my_list.pop(1))

print("ELIMINA POR INDICE")
del my_list[0]
print(my_list)

print("COPIAR UNA LISTA")
my_new_list = my_list.copy()

my_list.clear()
print(my_new_list)
print(my_list)

print("DAR LA VUELTA A LA LISTA")
my_new_list.reverse()
print(my_new_list)

print("ORDENACION DE FORMA ALFABETICA")
my_new_list.sort()
print(my_new_list)

print("SUB LISTAS")
print(my_new_list[1:2])