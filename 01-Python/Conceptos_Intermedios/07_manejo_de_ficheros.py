#Manejo de ficheros
import os

# .txt file si se pone w se puede escribir y leer y escribir es w+

txtfile = open("my_file", "w+")
txtfile.write("\ny el lenguaje que estoy estudiando es Python\n aunque me encanta Kotlin")

#print(txtfile.read())
#print(txtfile.read(10))

#print(txtfile.readline())
#print(txtfile.readline())

for element in txtfile.readlines() :
    print(element)

print(txtfile.readline())
txtfile.close()

#os.remove("Conceptos_Intermedios/my_file