#Ejercicio 23:
#área de un polígono regular
#Un polígono es regular si sus lados tienen la misma longitud y los ángulos entre todos
#Los lados adyacentes son iguales. El área de un polígono regular se puede calcular usando
#la siguiente fórmula, donde s es la longitud de un lado yn es el número de lados:
#área = n × s^2 /4 × tan (π/n)
#Escriba un programa que lea s y n del usuario y luego muestre el área de un
#polígono regular construido a partir de estos valores.
import math
n=int(input("Ingrese numero de lados:"))
s=int(input("ingrese el apotema:"))
area= (n * math.pow(s, 2))/ ( 4 * math.tan(math.pi))
print("El area de tu poligono es %.4f" % area)