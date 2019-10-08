# -*- coding: utf-8 -*-
"""
Created on Tus Oct  5 11:20:50 2019

@author: poloXO
"""

#Ejercicio 14: unidades de altura
#Muchas personas piensan en su altura en pies y pulgadas, incluso en algunos países que
#utiliza principalmente el sistema métrico. Escriba un programa que lea un número de pies de
#el usuario, seguido de varias pulgadas. Una vez que se leen estos valores, su programa
#debe calcular y mostrar el número equivalente de centímetros.
#Sugerencia: un pie mide 12 pulgadas. Una pulgada es 2.54 centímetros.
pies=float(input("Inserte el total de pies:"))
pulgadas=float(input("Inserte el total de pulgadas:"))
ft=pies*12
IN=ft+pulgadas
cm=IN*2.54
print("total de pulgadas",IN)
print("la equivalencia es:",cm,"cm")