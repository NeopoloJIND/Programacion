# -*- coding: utf-8 -*-
"""
Created on Tus Oct  5 11:20:50 2019

@author: poloXO
"""
#Ejercicio 15: 
#Unidades de distancia
#En este ejercicio, creará un programa que comienza leyendo una medida
#en pies del usuario. Entonces su programa debe mostrar la distancia equivalente en
#pulgadas, yardas y millas. Use Internet para buscar los factores de conversión necesarios
#si no los tienes memorizados.
pies=float(input("Ingrese la cantidad de pies:"))
Pulgadas=pies*12
Yardas=pies/3
Millas=pies/5280
print("Equivalente en pulgadas", Pulgadas)
print("Equivalente en yardas", Yardas)
print("Equivalente en millas", Millas)