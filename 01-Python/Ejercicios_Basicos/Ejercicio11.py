# Escribe un programa que cuente cuántas vocales tiene una frase ingresada por el usuario.

my_phrase = input("Introduce una frase: ").lower()

my_vocals="aeiou"

my_sum = 0
for vocals in  my_phrase:
    if vocals in my_vocals:
        my_sum+=1
print(f"Las vocales que hay en la frase {my_phrase} es de {my_sum} ")