# Solicita al usuario una frase y un número. Luego, muestra la frase en mayúsculas si el número es par y en minúsculas si es impar.

my_phrase = input("Introduce una frase: ")
my_number = int(input("Introduce un numero: "))

if my_number % 2 == 0 :
    print(my_phrase.upper())

else: print(my_phrase.lower())