# Excepciones

numer_one = 5
numer_two = 7

numer_two = "1"
try:
    print(numer_one + numer_two)
except TypeError: #Se ejecuta solo si se ejecuta TypeError
    print("Se ha producido un error")
