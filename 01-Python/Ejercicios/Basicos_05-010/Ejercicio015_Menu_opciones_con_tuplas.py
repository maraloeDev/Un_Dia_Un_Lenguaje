# Diseña un programa que muestre
# un menú de opciones almacenado en una tupla y permita al usuario elegir una opción válida.
# Si la opción no es válida, debe volver a pedir una entrada hasta que el usuario ingrese una correcta.

my_tuple = ("1. Ver Lista", "2. Borrar Lista", "3. Modificar lista")

# Repite el bucle, hasta que se introduzca una opcion
while True :
    for my_values in my_tuple:
        print(f"\n {my_values}")
    my_option =input("Seleccione una opcion:")

#Si la opcion seleccionada es 1 2 o 3
    if my_option in ("1" , "2" ,"3"):
        print(f"La opcion marcada es la {my_option}")
        break
    else:
        print("No se ha seleccionado ninguna opcion")

