# Crea un programa que genere una contraseña aleatoria de 8 caracteres.
import random
import string

def generar_contrasena(longitud=8):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choices(caracteres, k=longitud))
    return contraseña

print(generar_contrasena())
