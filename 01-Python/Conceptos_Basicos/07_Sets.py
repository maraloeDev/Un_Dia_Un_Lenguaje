#SETS no es una estructura desordenada y no admite repetidos

my_set = ()
my_other_set = {}

print(type(my_other_set)) #Inicialmente es un diccionario

my_other_set = {"Eduardo",25, "maraloedev"}
print(type(my_other_set))
print(my_other_set)

print(len(my_other_set))

my_other_set.add("Calle la Petunia")
print(my_other_set)

my_other_set.add("Calle la Petunia")
print(my_other_set)

print("BUSCAR DATO")
print("Eduardo" in  my_other_set) # Existe en...
print("Eduardi" in  my_other_set)

print("ELIMINAR DATOS")
print(my_other_set)
my_other_set.remove("Eduardo")
print(my_other_set)

print("LIMPIAR LA LISTA")
my_other_set.clear()
print(len(my_other_set))