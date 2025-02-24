# Crea un programa que cuente cuántas veces aparece una palabra en una frase ingresada por el usuario.

my_phrase = input("Introduce una frase: ")
my_word = input("Introduce la palabra que quieres buscar: ")
print(f"En la frase {my_phrase} la palabra {my_word} aparece un total de {my_phrase.count(my_word)} veces")