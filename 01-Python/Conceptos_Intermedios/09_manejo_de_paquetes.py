# Manejo de paquetes

#pip es para

import numpy

print(numpy.version.version)

numpy_array = numpy.array([17,7,7,8,5,4,1,55,98,74,12])
print(type(numpy_array))

print(numpy_array * 2)


# pip list aparece la lista de paquites instalados
# pip uninstall desinstalar paquetes
# pip show numpy

import requests

response = requests.get("https://zelda.fanapis.com/api/games?name=The Legend of Zelda: Oca")
print(response.status_code)
print(response.json())
