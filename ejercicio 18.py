# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 20:28:19 2019

@author: poloXO
"""
#Ejercicio 18:Volumen de un cilindro
#(15 Líneas)
#El volumen de un cilindro se puede calcular multiplicando el área de su
#base por su altura. Escriba un programa que lea el radio del cilindro, junto con
#su altura, desde el usuario y calcula su volumen. Mostrar el resultado redondeado a uno
#decimal.
#volumen cilindro =(radio*altura)
import math

altura=int(input("Ingrese la Alturadel cilindro:"))
radio=int(input("Ingrese el Radio del cilindro:"))   
volumen=math.pi*radio**2*altura 
print("El volumen del cilindro es:",(volumen))