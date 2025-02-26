## Lambdas

sum_two_values  = lambda first_value, second_value: print(first_value + second_value)
sum_two_values(12,12)

multiply_values= lambda first_value, second_value:first_value * second_value -3
print(multiply_values(5,7))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value
print(sum_three_values(5)(1,2))