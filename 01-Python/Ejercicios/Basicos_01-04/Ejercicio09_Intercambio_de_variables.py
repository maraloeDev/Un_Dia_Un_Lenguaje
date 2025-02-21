# Solicita al usuario dos valores en variables diferentes
# e intercámbialos sin usar una tercera variable, mostrando el resultado.

my_variable_one = int(input("Introduce un numero: "))
my_variable_two = int(input("Introduce un numero: "))

print(f"La variable 1, vale ahora {my_variable_one}")
print(f"La variable 2, vale ahora {my_variable_two}")

my_variable_one = my_variable_two
my_variable_two = my_variable_one

print(f"La variable 1, vale una vez cambiada {my_variable_one}")
print(f"La variable 2, vale una vez cambiada {my_variable_two}")