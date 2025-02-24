# Crea un programa que pida al usuario un número y muestre su tabla de multiplicar.

my_number = int(input("Introduce un numero: "))

print(f"Tabla de multiplicar del {my_number}: ")

for number in range(1,10):
    print(f"{my_number} X {number} = " ,(my_number * number))