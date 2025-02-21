# Crea un programa que permita gestionar un inventario de productos utilizando un diccionario.
# El programa debe permitir
# agregar,
# eliminar y
# actualizar productos, además de mostrar el inventario completo.

my_dict = {"Manzana": 2.45, "Cereales": 2.23, "Sarten": 20}

while True:
    my_option = int(input(" 1-Agregar producto\n"
                          " 2-Eliminar productos\n"
                          " 3-Mostrar productos\n"
                          " 4-Salir\n"
                          " Introduce un numero: "))

    if my_option == 4:
        print("Saliendo del programa...")
        break

    match my_option:
        case 1:
            print("AGREGAR PRODUCTOS")
            my_new_name_product = input("Introduce un nombre de producto: ")
            my_new_price_product = float(input("Introduce un precio de producto: "))
            my_dict.update({my_new_name_product: my_new_price_product})
            print("Producto agregado:", my_dict)

        case 2:
            print("ELIMINAR PRODUCTOS")
            delete_product = input("Introduce un nombre de producto para eliminar: ")
            if delete_product in my_dict:
                my_dict.pop(delete_product)
                print(f"Producto eliminado: {delete_product}")
            else:
                print(f"El producto {delete_product} no existe.")
            print("Productos actuales:", my_dict)

        case 3:
            print("MOSTRAR PRODUCTOS")
            for producto, precio in my_dict.items():
                print(f"{producto}: {precio}")
