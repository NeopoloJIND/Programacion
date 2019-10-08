# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 20:37:44 2019

@author: poloXO
"""
#Ejercicio 21: área de un triángulo
#(13 líneas)
#El área de un triángulo se puede calcular usando la siguiente fórmula, donde (b) es el
#longitud de la base del triángulo, y (h) es su altura:
#área = b × h/2
#Escriba un programa que permita al usuario ingresar valores para byh. El programa
#luego debe calcular y mostrar el área de un triángulo con longitud base (b) y altura( h).

Base=input("Inserte la  base: ")
altura=input("Inserte la altura: ")
Area=int (Base) * int (altura) / 2.0
print ("La area es: ", str  (Area))
