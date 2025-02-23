# Escribe un programa que determine si un número ingresado por el usuario es par o impar.

my_number_par = int(input("Introduce un numero: "))

if (my_number_par % 2) == 0 :
    print(f"El {my_number_par} es par")
else:
    print(f"El {my_number_par} es impar")