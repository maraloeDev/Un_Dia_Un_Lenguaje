# Escribe un programa que determine si una palabra ingresada es un palíndromo.

my_word = input("Introduce una palabra: ").lower()

my_reverser_word = my_word[::-1]

if my_word == my_reverser_word :
    print(f"La palabra {my_word} es palindroma")
else:
    print(f"La palabra {my_word} no es palindroma")