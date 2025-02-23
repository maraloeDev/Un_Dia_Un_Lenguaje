# Crea un programa que solicite un número y calcule su factorial.

my_number_factorial =int(input("Introduce un numero: "))

factorial = 1
for my_number in range(1, my_number_factorial + 1):
    factorial *= my_number

print(f"El factorial de {my_number} es: {factorial}")