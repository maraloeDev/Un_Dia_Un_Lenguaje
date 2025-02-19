## Calculadora simple
# Crea un programa que solicite al usuario dos números y realice las cuatro operaciones básicas
# (suma, resta, multiplicación y división), mostrando los resultados en pantalla.
##

#Pido los numeros con un input, y casteo la respuesta a int
number_one = int(input("Introduce un numero: "))
number_two = int(input("Introduce un numero: "))

print(f"SUMA {number_one} + {number_two} = ", (number_one + number_two))
print(f"RESTA {number_one} - {number_two} = ", (number_one - number_two))
print(f"MULTIPLICACIÓN {number_one} * {number_two} = ", (number_one * number_two))
print(f"DIVISION {number_one} / {number_two} = ", (number_one / number_two))
