#Solicita al usuario su edad actual y un número de años a futuro. Luego, muestra cuántos años tendrá después de ese tiempo.

my_actually_age=int(input("Introduce tu edad actual: "))
my_future_age=int(input("Introduce tu numero de años en el futuro: "))

print(f"La edad que tendras dentro de {my_future_age} años es de {my_actually_age + my_future_age}")