#Pide al usuario tres números y muestra el resultado de sumarlos, multiplicarlos y calcular el promedio.

my_number_one = int(input("Introduce un numero: "))
my_number_two = int(input("Introduce un numero: "))
my_number_tree = int(input("Introduce un numero: "))

my_sum =  my_number_one + my_number_two + my_number_tree
my_mutipication =  my_number_one * my_number_two * my_number_tree
my_promedy = my_sum /3

print (f"La suma de los numeros introducidos son: {my_sum}")
print (f"La multiplicación de los numeros introducidos son: {my_mutipication}")
print (f"El promedio de los numeros introducidos son: {my_promedy}")
