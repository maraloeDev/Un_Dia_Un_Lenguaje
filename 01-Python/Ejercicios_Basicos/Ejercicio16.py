# Crea un programa que genere los primeros 10 términos de la serie de Fibonacci.

def fibonacci(n):
    fib_series = [0, 1]
    for _ in range(n - 2):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

# Generar los primeros 10 términos de Fibonacci
primeros_10 = fibonacci(10)
print(primeros_10)
