# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 20:37:54 2019

@author: poloXO
"""
#Ejercicio 22: área de un triángulo (de nuevo)
#(16 líneas)
#En el ejercicio anterior, creó un programa que calculaba el área de un triángulo
#cuando se conocía la longitud de su base y su altura. También es posible calcular
#El área de un triángulo cuando se conocen las longitudes de los tres lados. Deje s1, s2 y s3
#ser la longitud de los lados. Sea (s = (s1 + s2 + s3) / 2). Entonces el área del triángulo
#se puede calcular usando la siguiente fórmula:
#área =sqrt(s × (s - s1) × (s - s2) × (s - s3))
#Desarrolle un programa que lea las longitudes de los lados de un triángulo del usuario y
#Muestra su área.
import math

A= float (input("ingrese el primer lado del trangulo;")) 
B= float (input ("ingrese el segundo lado del triangulo:"))
C= float (input ("ingrese el tercer lado del triangulo:"))

if (A+B)>C and (A+C)>B and (B+C)>A:
   print("Los lados corresponden a un triangulo")    
else:
    print ("Los lados no corrsponden a un triangulo")

S=(A+B+C)/2
area =(S*(S-A)*(S-B)*(S-C))**0.5
print ("El area del triangulo es:" ,area)
