# Pide al usuario el precio de un producto y un porcentaje de descuento.
# Calcula el precio final después del descuento y muéstralo con dos decimales.

my_price = float(input("Introduce un precio: "))
my_porcentage = float(input("Introduce un descuento: "))

my_discount = my_price * (my_porcentage / 100)
my_total = my_price - my_discount

print(f"El descuento total es de {my_discount:.2f}")
print(f"El precio final después del descuento es de {my_total:.2f}")