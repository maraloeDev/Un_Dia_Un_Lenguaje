## Funciones de orden superior son funciones que hacen cosas con otras funciones
from functools import reduce


def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


def sum_two_values_and_add_one(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)


print(sum_two_values_and_add_one(5, 2, sum_one))
print(sum_two_values_and_add_one(5, 2, sum_five))


## Closures es una funcion que retorna una funcion

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value

    return add


add_closure = sum_ten(1)

print(add_closure(5))
print(sum_ten(5)(1))

## Funciones de orden superior del sistema todas necesitan un iterable
numbers = [2, 5, 10, 21, 3, 30]


## Map recorre todos los valores y ejecuta una funcion sobre ellos para modiificar su valor
def multiply_two(number):
    return number * 2


print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))


# Filter recorre todos los valores y ejecuta una funcion que devuelve true o false para saber como filtrar los valores de la lista opera el valor mas el acumulado
def filter_grater_than_ten(number):
    if number > 10:
        return True
    return False


print(list(filter(lambda number: number > 10, numbers)))


# Reduce opera entre los valores que va recorriendo
def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value


print(reduce(sum_two_values, numbers))
