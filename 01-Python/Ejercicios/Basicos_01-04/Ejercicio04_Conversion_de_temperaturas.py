#Pide al usuario una temperatura en grados Celsius y conviértela a Fahrenheit, mostrando el resultado con un mensaje descriptivo.

my_temperature_celsius= float(input("Introduce una temperatura en grados celsius: "))

my_result = (my_temperature_celsius * 9/5) + 32

print(f"El resultado de convertir los grados celsius a Farenheith es de  {my_result}")