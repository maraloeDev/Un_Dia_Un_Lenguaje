# Crea un programa que permita gestionar un inventario de productos
# usando un diccionario donde
# las claves sean los nombres de los productos y
# los valores sean listas con la cantidad disponible y el precio unitario.
# El programa debe permitir
# agregar productos,
# actualizar cantidades,
# eliminar productos
# y mostrar el inventario completo.

my_dict = {"Manzanas": [2, 2.80], "Mandarinas": [12, 5.55], "Pepinillos": [55, 2.55]}

while True:
    print("Selecciona una opción\n"
          "1. Agregar productos\n"
          "2. Actualizar cantidades\n"
          "3. Eliminar productos\n"
          "4. Mostrar productos\n"
          "5. Salir")

    my_option = int(input("Selecciona una opción: "))

    if my_option == 1:
        my_product_name = input("Introduce el nombre: ")
        my_product_stock = int(input("Introduce la cantidad disponible del producto: "))
        my_product_price = float(input("Introduce el precio unitario del producto: "))
        my_dict.update({my_product_name: [my_product_stock, my_product_price]})
        print(f"Producto agregado correctamente\n {my_dict}")

    elif my_option == 2:
        my_product_name_modify = input("Introduce el nombre del producto a modificar: ")

        if my_product_name_modify in my_dict:
            my_new_amount = int(input("Introduce la nueva cantidad: "))
            my_dict[my_product_name_modify][0] = my_new_amount  # Actualiza la cantidad en la posición 0
            print(f"Cantidad actualizada correctamente\n {my_dict}")
        else:
            print("El producto no existe en el inventario.")

    elif my_option == 3:
        my_p = input("Introduce el nombre del producto a eliminar: ")

        if my_p in my_dict:
            del my_dict[my_p]
            print(f"Producto eliminado correctamente\n {my_dict}")
        else:
            print("El producto no existe en el inventario.")

    elif my_option == 4:
        print("Inventario actual:")
        for producto, datos in my_dict.items():
            print(f"{producto}: Cantidad: {datos[0]}, Precio: {datos[1]:.2f}")

    elif my_option == 5:
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida, intenta de nuevo.")
