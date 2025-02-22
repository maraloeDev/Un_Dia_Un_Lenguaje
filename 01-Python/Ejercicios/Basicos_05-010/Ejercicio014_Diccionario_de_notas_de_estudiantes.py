# Crea un diccionario donde las claves sean nombres de estudiantes y los valores sean listas con sus calificaciones.
# Luego, muestra el promedio de calificaciones de cada estudiante.

my_dict = {"Pablo":[10,8,6], "Enrique":[5,6,4],"Eduardo": [10,8.75,4], "Juan": [5,4,7]}

for my_students, my_values in my_dict.items():
    promedio = sum(my_values) / len(my_values)
    print(f"El promedio de {my_students} es de {promedio:.1f}"  )

