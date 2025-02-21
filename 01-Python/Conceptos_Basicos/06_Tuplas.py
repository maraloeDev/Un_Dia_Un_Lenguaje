#TUPLAS es un conjunto de valores y es inmutable (No se pueden cambiar los valores)

my_tuple = (35,1.85,"Eduardo", "Martín-Sonseca", "Eduardo")
my_other_tuple = (35,60,30)
print(my_tuple)

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Eduardo")) ##CUENTA LAS VECES QUE APARECE UNA PALABRA
print(my_tuple.index(35))
print(my_tuple.index("Eduardo"))

my_sum_tuple = my_other_tuple + my_tuple
print(my_sum_tuple)

print("BUSCA ELEMENTOS DESDE UN ELEMENTO HASTA OTRO")
print(my_sum_tuple[0:6])

my_sum_tuple = list(my_sum_tuple)
print(type(my_sum_tuple))

my_sum_tuple[0] = "HOLA QUE TAL"
print(my_sum_tuple)

my_sum_tuple = tuple(my_sum_tuple)
print(type(my_sum_tuple))