## Expresiones regulares inspeccionan una cadena de texto

import re
from shlex import split

my_string="Esta es la leccion numero 8: Expresiones regulares"
my_other_string="Esta no es la leccion numero 7:manejo de ficheros"

#match es para saber si un texto, tiene alguna palabra en concreto, empieza a buscar desde el principio
match = re.match("Esta es la leccion", my_string, re.I)
print(match)
start, end  = match.span()
print(my_string[start:end])



print(re.match("Esta es la leccion", my_other_string))

if match != None:
    print(match)
    start, end  = match.span()
    print(my_string[start:end])


print(re.match("Expresiones regulares", my_string))

#Search
search = re.search("Expresiones regulares", my_string, re.I)
print(search)
start, end  = match.span()
print(my_string[start:end])

##findAll busca las veces que a entontrado la palabra, y las mete en una lista
findAll = re.findall("leccion", my_string, re.I)
print(findAll)

#Split busca un patron entre lo que le pases, y lo divide
split = re.split(":", my_string)
print(split)

#sub sirve para sustituir una parlabra por otra
print(re.sub("[l|L]eccion", "LECCION", my_string))
print(re.sub("Expresiones regulares", "RegEx", my_string))


