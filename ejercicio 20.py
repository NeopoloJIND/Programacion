# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 20:37:42 2019

@author: poloXO
"""
#Ejercicio 20: Ley de Gas Ideal
#(19 Líneas)
#La ley de gas ideal es una aproximación matemática del comportamiento de los gases como
#cambio de presión, volumen y temperatura. Por lo general, se indica como:
#PV = nRT
#donde P es la presión en Pascales, V es el volumen en litros, n es la cantidad de
#sustancia en moles, R es la constante de gas ideal, igual a 8.314 J
#mol K, y T es la temperatura en grados Kelvin.
#Escriba un programa que calcule la cantidad de gas en moles cuando el usuario suministra
#La presión, el volumen y la temperatura. Prueba tu programa determinando el número
#de moles de gas en un tanque de buceo. Un tanque de buceo típico contiene 12 litros de gas a
#una presión de 20,000,000 Pascales (aproximadamente 3,000 PSI). La temperatura ambiente es 10
#aproximadamente 20 grados Celsius o 68 grados Fahrenheit.
# 1) Introducción a los ejercicios de programación
#Sugerencia: una temperatura se convierte de Celsius a Kelvin al agregar 273.15 lo.
# Para convertir una temperatura de Fahrenheit a Kelvin, deduzca 32 de ella,
#multiplícalo por 59
#y luego agregue 273.15.

R=8.314
T=int(input("Ingrese la temperatura:"))
P=int(input("Ingrese la precion en pascales:"))
V=int(input("Ingrese el volumen en litro:"))
operacion= (P*V)/(R*T)
print("Tu resultado en moles es:", operacion)
