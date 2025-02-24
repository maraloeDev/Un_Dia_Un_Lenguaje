# Crea un programa que convierta una lista de grados Celsius a Fahrenheit.

my_list = [14,5,41,20,17,32,30]

print(f"La lista de los grados Celius es: \n{my_list}")
my_new_list_fahrenheit = []

for list_fahrenheit in my_list:
    my_new_list_fahrenheit.append((list_fahrenheit * 9/5) +32)
print(f"Las temperaturas pasadas a Fahrenheit son \n{my_new_list_fahrenheit}")
