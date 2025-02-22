## Funciones resuelve un problema en concreto

def my_function():
    print("Esto es una funcion")

my_function()
my_function()
my_function()

def sum_two_values (first_number, second_number):
    print(first_number + second_number)

sum_two_values(5,5)
sum_two_values(14,20)
sum_two_values(919192929.03,1212121212.12)

def sum_two_values_with_return(first_value, second_value):

    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values_with_return(5,5)
print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(name="Eduardo",surname="Martín-Sonseca")

def print_name_with_default(name, surname, alias="Sin alias"): #Se pueden establecer un valor por defecto
    print(f"{name} {surname} {alias}")

print_name_with_default("Eduardo","Martín-Sonseca")


def print_upper_texts(*texts): #El asterisco funciona para establecer infinitos parametros
    for element in texts:
        print(element)


print_upper_texts("Hola", "Python", "maraloedev")