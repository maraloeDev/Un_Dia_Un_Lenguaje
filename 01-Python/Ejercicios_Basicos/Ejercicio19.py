# Escribe un programa que elimine los elementos duplicados de una lista.

my_list = [1,4,7,5,8,8,7,4,1,2,5,6,9,8,5,4,1]

unique_items = []
duplicates = set()

for num in my_list:
    if num in unique_items:
        duplicates.add(num)
    else:
        unique_items.append(num)

print(f"Lista sin duplicados: {unique_items}")
print(f"Los números repetidos son: {list(duplicates)}")