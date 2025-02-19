#Strings

my_String = "Mi String"
my_other_string="My otro String"
print(len(my_String))
print(len(my_other_string))

print(my_String + " " + my_other_string)

my_new_line_string="Este es un string con salto dde linea"
print(my_new_line_string)

my_tab_string="\tEste es un string con salto dde linea"
print(my_tab_string)

my_scape_string="\tEste es un string \n escapado"
print(my_scape_string)

#Formateo

name, surname, age="Eduardo", "Martin-Sonseca", 25
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

language = "Python"

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))