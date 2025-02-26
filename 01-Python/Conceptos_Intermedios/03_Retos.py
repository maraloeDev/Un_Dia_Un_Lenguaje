## RETOS
from operator import index


## EL FAMOSO "FIZZ BUZZ"
## Escribe un programa que muestre por consola (con un print) los
## números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
## - Múltiplos de 3 por la palabra "fizz".
## - Múltiplos de 5 por la palabra "buzz".
## - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".


def fizzbuzz():
    for elements in range(1, 101):
        if elements % 3 == 0 and elements % 5 == 0:
            print("fizzbuzz")
        elif elements % 5 == 0:
            print("buzz")

        elif elements % 3 == 0:
            print("fizz")
        else:
            print(elements)

fizzbuzz()

## ES UN ANAGRAMA
## Escribe una función que reciba dos palabras (String) y retorne
## verdadero o falso (Bool) según sean o no anagramas.
## - Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
## - NO hace falta comprobar que ambas palabras existan.
## - Dos palabras exactamente iguales no son anagrama.

def anagrama(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == word_two.lower()

print(anagrama("Amor", "Roma"))


## LA SUCESION DE FIBONACCI
# Escribe un programa que imprima los 50 primeros números de la sucesión
# de Fibonacci empezando en 0.
# - La serie Fibonacci se compone por una sucesión de números en
#   la que el siguiente siempre es la suma de los dos anteriores.
#   0, 1, 1, 2, 3, 5, 8, 13..

def fibonacci():
    prev = 0
    next = 1
    for number in range(51):
        print(prev)
        fib = prev + next
        prev = next
        next = fib


fibonacci()

## NUMERO PRIMO
## Escribe un programa que se encargue de comprobar si un número es o no primo.
## Hecho esto, imprime los números primos entre 1 y 100.

def number_prime():
    for number in range(1,101):
        if number >= 2:

            is_divisible = False

            for element in range(2,number):
                if number % element == 0:
                    is_divisible = True

            if not is_divisible:
                print(number)

number_prime()

## INVIETIENDO CADENAS


## Crea un programa que invierta el orden de una cadena de texto
## sin usar funciones propias del lenguaje que lo hagan de forma automática.
## - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"


def reverse(text):
    text_lenth= len(text)
    reversed_text= ""

    for index in range(0,text_lenth):
        reversed_text += text[text_lenth - index -1]

    return reversed_text


##FORMA FACIL
## print(text)
##print(text[::-1])
print(reverse("Hola mundo"))
