# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 23:47:07 2019

@author: poloXO
"""

#Ejercicio 32: ordenar 3 enteros
#Cree un programa que lea tres enteros del usuario y los muestre ordenados
#orden (de menor a mayor). Usa las funciones min y max para encontrar el más pequeño
#y valores más grandes. El valor medio se puede encontrar calculando la suma de los tres
#valores, y luego restando el valor mínimo y el valor máximo.

a=int (input("Inserte su primer numero:"))
b=int (input("Inserte su segundo numero:"))
c=int (input("Inserte su tercer numero"))
MIN = min (a,b,c)
MAX = max (a,b,c)
MED= a+b+c -MIN-MAX

print(" Los numeros en orden son:")
print("",MIN)
print("",MED)
print("",MAX)
